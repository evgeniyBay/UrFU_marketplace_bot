from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = [[KeyboardButton(text="Купить"),
             KeyboardButton(text="Продать"),
             KeyboardButton(text="Мои товары")]]

kb = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
