import asyncio
import os

from aiohttp import web
from aiogram import Bot, Dispatcher, types
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = f"https://academy-bot.onrender.com{WEBHOOK_PATH}"

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher()


@dp.message()
async def handle_message(message: types.Message):
    await message.answer("✅ Бот работает через Webhook!")


async def on_startup(app):
    await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown(app):
    await bot.delete_webhook()


async def create_app():
    app = web.Application()
    SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path=WEBHOOK_PATH)
    setup_application(app, dp, bot=bot)

    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

    return app


if __name__ == "__main__":
    web.run_app(create_app(), port=int(os.environ.get("PORT", 10000)))
