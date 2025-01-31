from aiogram import types, Dispatcher
from app.app.services.imeicheck import check_imei
from app.app.utils.imei_validator import is_valid_imei


async def handle_imei(message: types.Message):
    imei = message.text.strip()

    if not is_valid_imei(imei):
        await message.answer(
            "Невалидный IMEI. Пожалуйста, проверьте и попробуйте снова."
        )
        return

    await message.answer("Проверяю IMEI, пожалуйста, подождите...")

    try:
        result = await check_imei(imei)
    except Exception as e:
        await message.answer(f"Ошибка при проверке IMEI: {str(e)}")
        return

    if "error" in result:
        await message.answer(f"Ошибка при проверке IMEI: {result['error']}")
    else:
        formatted_result = "\n".join(f"{key}: {value}" for key, value in result.items())
        await message.answer(f"Результат проверки IMEI:\n{formatted_result}")


def register_imei_handler(dp: Dispatcher):
    dp.message.register(
        handle_imei,
        lambda message: (
            message.content_type == types.ContentType.TEXT
            and message.text
            and len(message.text.strip()) == 15
            and message.text.strip().isdigit()
        ),
    )
