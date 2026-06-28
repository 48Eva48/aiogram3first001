import asyncio
from aiogram import types, filters, Router, F

filter_router = Router()

@filter_router.message((F.text.lower() == "как дела") | (F.text.lower() == "как дела?"))
async def how_are_you_handler(message: types.Message) -> None:
    await message.reply(f"У меня все нормально, у тебя дела как, {message.from_user.full_name}?")

@filter_router.message()
async def reply_handler(message: types.Message) -> None:
    await message.reply(message.text)
