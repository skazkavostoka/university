import aiogram
from aiogram import Bot, Dispatcher
from dotenv import find_dotenv, load_dotenv
import logging
import asyncio
import os


from bot_addition.viewer import viewer_router

load_dotenv(find_dotenv())

logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv('token'), parse_mode='HTML')

dp = Dispatcher()

dp.include_router(viewer_router)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())