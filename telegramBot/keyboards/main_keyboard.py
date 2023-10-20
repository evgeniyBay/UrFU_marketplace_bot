from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = [[KeyboardButton(text="Купить"),
             KeyboardButton(text="Продать")]]

kb = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
