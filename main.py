import asyncio
import os
from aiohttp import web
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = f"https://academy-bot.onrender.com{WEBHOOK_PATH}"

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

WELCOME_TEXT = (
    "👋 <b>Добро пожаловать в закрытый канал Академии «Бенефактор» Игоря Стрельникова и Максима Кучерова!</b>\n\n"
    "Здесь вы получите доступ к вводным бесплатным урокам, актуальным новостям Академии, сможете записаться на предстоящие сессии с нашими экспертами (в процессе технической настройки), "
    "задать вопросы в специальной группе, участвовать в видеовстречах и — главное — понять, подходит ли вам наше обучение.\n\n"
    "✍️ <b>Пожалуйста, напишите в ответ несколько слов:</b>\n"
    "какую пользу вы хотели бы получить и какие боли или задачи хотели бы решить с нашей помощью."
)

@dp.message()
async def handle_message(message: Message):
    await message.answer(WELCOME_TEXT)

async def on_startup(app: web.Application):
    await bot.set_webhook(WEBHOOK_URL)

async def on_shutdown(app: web.Application):
    await bot.delete_webhook()

async def create_app():
    app = web.Application()
    SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path=WEBHOOK_PATH)
    setup_application(app, dp, bot=bot)
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)
    return app

if __name__ == "__main__":
    web.run_app(create_app(), host="0.0.0.0", port=int(os.getenv("PORT", 10000)))
