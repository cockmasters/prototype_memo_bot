import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

from settings import bot_settings

bot = Bot(token=bot_settings.TOKEN_TG)
dp = Dispatcher()


@dp.message(Command("start"))
async def hello(message: types.Message):
    await message.answer("Привет")


async def start():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(start())
