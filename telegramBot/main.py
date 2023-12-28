import asyncio

from aiogram import Bot, Dispatcher
from handlers import main_handler, sell_handler, product_list_handler
from telegramBot.sql import sqlite

TOKEN = "1750341065:AAEFiU6RXZbV1dDK98SktrBSyQ5waOWSg0M"
bot = Bot(TOKEN)


async def on_startup():
    await sqlite.db_start()


async def main():
    dp = Dispatcher()
    dp.include_router(main_handler.router)
    dp.include_router(sell_handler.router)
    dp.include_router(product_list_handler.router)
    await on_startup()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
