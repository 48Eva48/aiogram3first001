import asyncio
from aiogram import types, filters, Router

commands_router = Router()

@commands_router.message(filters.CommandStart())
async def start_handler(message: types.Message) -> None:
    await message.answer(f"Yello, {message.from_user.full_name}")

@commands_router.message(filters.Command("about"))
async def about_handler(message: types.Message) -> None:
    await message.answer(f"Alama - это бот, который создан для изучения 3-й версии aiogram.")