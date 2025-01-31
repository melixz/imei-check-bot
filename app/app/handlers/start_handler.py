from aiogram import types, Dispatcher
from aiogram.filters import Command


async def cmd_start(message: types.Message):
    await message.answer(
        "Добро пожаловать в IMEI-бот!\n"
        "Отправьте IMEI для проверки, и я предоставлю информацию о нём."
    )


def register_start_handler(dp: Dispatcher):
    dp.message.register(cmd_start, Command(commands=["start"]))
