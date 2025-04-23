import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web
import os

TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = f"https://academy-bot.onrender.com{WEBHOOK_PATH}"

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher()

@dp.message()
async def echo_handler(message: types.Message) -> None:
    await message.answer("Бот работает по Webhook 🎯")

async def on_startup(app):
    await bot.set_webhook(WEBHOOK_URL)

async def on_shutdown(app):
    await bot.delete_webhook()

async def main():
    app = web.Application()
    SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path=WEBHOOK_PATH)
    setup_application(app, dp, bot=bot)
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)
    return app

if __name__ == "__main__":
    web.run_app(main(), port=1000import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web
import os

TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = f"https://academy-bot.onrender.com{WEBHOOK_PATH}"

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher()

@dp.message()
async def echo_handler(message: types.Message) -> None:
    await message.answer("Бот работает по Webhook 🎯")

async def on_startup(app):
    await bot.set_webhook(WEBHOOK_URL)

async def on_shutdown(app):
    await bot.delete_webhook()

async def main():
    app = web.Application()
    SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path=WEBHOOK_PATH)
    setup_application(app, dp, bot=bot)
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)
    return app

if __name__ == "__main__":
    web.run_app(main(), port=10000)import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web
import os

TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = f"https://academy-bot.onrender.com{WEBHOOK_PATH}"

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher()

@dp.message()
async def echo_handler(message: types.Message) -> None:
    await message.answer("Бот работает по Webhook 🎯")

async def on_startup(app):
    await bot.set_webhook(WEBHOOK_URL)

async def on_shutdown(app):
    await bot.delete_webhook()

async def main():
    app = web.Application()
    SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path=WEBHOOK_PATH)
    setup_application(app, dp, bot=bot)
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)
    return app

if __name__ == "__main__":
    web.run_app(main(), port=10000)
