from aiogram import Bot, Dispatcher
from app.app.core.config import settings

bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)
