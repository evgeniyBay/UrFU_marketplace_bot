import sqlite3 as sq

from aiogram import Router, F, types
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

current_pos = 0
products = []


def get_product_kb():
    global current_pos, products

    keyboard = [[InlineKeyboardButton(text="<", callback_data="prev_product"),
                 InlineKeyboardButton(text=f"{current_pos + 1}/{len(products)}", callback_data="product_counter"),
                 InlineKeyboardButton(text=">", callback_data="next_product")]]

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


@router.message(F.text == "Мои товары")
async def get_product_list(message: Message):
    global products
    conn = sq.connect('products.db')
    cursor = conn.cursor()

    cursor.execute("SELECT title, cost, description, photo_id FROM products WHERE seller_id = ?",
                   (message.from_user.id,))

    products = cursor.fetchall()
    conn.close()

    await show_product_list(message)


@router.message()
async def show_product_list(message: Message):
    global current_pos, products

    title, cost, description, photo_id = products[current_pos]

    await message.answer_photo(photo_id,
                               caption=f"{title}, {cost}\n\n{description}",
                               reply_markup=get_product_kb())


@router.callback_query()
async def handle_product_button(query: CallbackQuery):
    global current_pos, products

    if query.data == "prev_product":
        current_pos -= 1
        if current_pos < 0:
            current_pos = len(products) - 1

    elif query.data == "next_product":
        current_pos += 1
        if current_pos >= len(products):
            current_pos = 0

    title, cost, description, photo_id = products[current_pos]

    media = types.InputMediaPhoto(media=photo_id,
                                  caption=f"{title}, {cost}\n\n{description}")

    from telegramBot.main import bot

    await bot.edit_message_media(media=media, message_id=query.message.message_id,
                                 reply_markup=get_product_kb(), chat_id=query.message.chat.id)
