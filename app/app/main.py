import asyncio
from aiogram.types import BotCommand
from app.app.core.bot import bot, dp
from app.app.handlers.start_handler import register_start_handler
from app.app.handlers.imei_handler import register_imei_handler
from app.app.middlewares.white_list import setup_middlewares


async def set_bot_commands():
    commands = [
        BotCommand(command="start", description="Начать работу с ботом"),
        BotCommand(command="check_imei", description="Проверить IMEI устройства"),
    ]
    await bot.set_my_commands(commands)


async def main():
    setup_middlewares(dp)

    register_start_handler(dp)
    register_imei_handler(dp)

    await set_bot_commands()

    print("Бот запущен и слушает обновления...")
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    asyncio.run(main())
