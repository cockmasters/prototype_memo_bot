import asyncio

from aiogram import Bot, Dispatcher, types

from log import start_log
from settings import bot_settings
from telegram_app.handlers import idea, start
from telegram_app.middlewares import LogMiddleware


async def main():
    bot = Bot(token=bot_settings.TOKEN_TG)
    dp = Dispatcher()
    dp.include_routers(start.router, idea.router)
    dp.update.middleware(LogMiddleware())
    start_log()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

