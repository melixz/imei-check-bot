from aiogram import types
from aiogram.dispatcher import dispatcher


def register_start_handler(dp: dispatcher):
    @dp.message_handler(commands=["start"])
    async def cmd_start(message: types.Message):
        await message.answer(
            "Добро пожаловать в IMEI-бот!\n"
            "Отправьте IMEI для проверки, и я предоставлю информацию о нём."
        )
