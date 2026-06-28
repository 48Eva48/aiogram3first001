import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers.commands import commands_router
from handlers.magic_filter import filter_router

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def main():
    dp.include_routers(commands_router, filter_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot job is stopped")