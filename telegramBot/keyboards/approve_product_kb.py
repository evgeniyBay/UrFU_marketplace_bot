from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = [[KeyboardButton(text="1❌"),
             KeyboardButton(text="2🔁"),
             KeyboardButton(text="3✅")]]

kb = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
