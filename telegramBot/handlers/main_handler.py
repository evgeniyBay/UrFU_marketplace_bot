from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards import main_keyboard

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer("<b>Привет! Давай начнём</b> 🛍\r\n\r\nНажми на кнопки ниже чтобы продать или купить!",
                         parse_mode='HTML', reply_markup=main_keyboard.kb)
