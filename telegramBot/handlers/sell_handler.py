import json
import random

import requests
from aiogram import Router, F
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from telegramBot.keyboards import main_keyboard, approve_product_kb
from telegramBot.main import bot, TOKEN
from telegramBot.sql import sqlite

router = Router()


class SellProduct(StatesGroup):
    choosing_name = State()
    choosing_cost = State()
    choosing_description = State()
    choosing_photo = State()

    approve_product = State()


def get_cancel_kb():
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Прервать создание объявления")]],
        resize_keyboard=True,
        one_time_keyboard=False)


@router.message(F.text == "Прервать создание объявления")
async def cancel(message: Message, state: FSMContext):
    if await state.get_state() is None:
        return
    await state.clear()
    await message.answer("Создание объявления прервано", reply_markup=main_keyboard.kb)


@router.message(F.text == "Продать")
async def sell(message: Message, state: FSMContext):
    await message.answer("Придумай название товара", reply_markup=get_cancel_kb())
    await state.set_state(SellProduct.choosing_name)


@router.message(SellProduct.choosing_name)
async def name_chosen(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    await message.answer("Назови цену товара")
    await state.set_state(SellProduct.choosing_cost)


@router.message(SellProduct.choosing_cost)
async def cost_chosen(message: Message, state: FSMContext):
    await state.update_data(cost=message.text)
    await message.answer("Придумай описание товара")
    await state.set_state(SellProduct.choosing_description)


@router.message(SellProduct.choosing_description)
async def description_chosen(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Пришли фото товара")
    await state.set_state(SellProduct.choosing_photo)


@router.message(SellProduct.choosing_photo)
async def description_chosen(message: Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)
    data = await state.get_data()

    await message.answer("Так выглядит ваш товар:")
    await message.answer_photo(data['photo'],
                               caption=f"{data['title']}, {data['cost']}\n\n{data['description']}")

    await message.answer(
        """1. Прервать создание объявления.\n\r2. Заполнить объявление заново.\n\r3. Выставить объявление.""",
        reply_markup=approve_product_kb.kb)
    await state.set_state(SellProduct.approve_product)


@router.message(SellProduct.approve_product)
async def description_chosen(message: Message, state: FSMContext):
    if message.text == "1❌":
        await cancel(message, state)

    if message.text == "2🔁":
        await message.answer("Придумай название товара",
                             reply_markup=get_cancel_kb())
        await state.set_state(SellProduct.choosing_name)

    if message.text == "3✅":
        id = random.randint(0, 100)
        data = await state.get_data()

        file = await bot.get_file(data['photo'])
        url = f"https://api.telegram.org/file/bot{TOKEN}/{file.file_path}"
        response = requests.get(url)

        await sqlite.create_product(product_id=id)
        await sqlite.edit_profile(state, product_id=id, seller_id=message.from_user.id, photo=response.content.hex())

        await state.clear()

        await message.answer("Ваш товар успешно выставлен на продажу!", reply_markup=main_keyboard.kb)

        product_info = {"product_id": id, "seller_id": message.from_user.id, "title": data['title'],
                        "cost": data['cost'], "description": data['description'], "photo": response.content.hex(),
                        "photo_id": data['photo']}

        json_file = json.dumps(product_info, indent=4)

        # with open("test.json", "w") as file:
        #     file.write(json_file)
        #
        # Image.open(BytesIO(bytes.fromhex(product_info['photo']))).save("test.png")
