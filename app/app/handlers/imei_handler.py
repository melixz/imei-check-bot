from aiogram import types, Dispatcher
from app.app.services.imeicheck import check_imei
from app.app.utils.imei_validator import is_valid_imei


def parse_imei_and_service(text: str):
    parts = text.strip().split()
    if len(parts) == 1:
        imei = parts[0]
        service_id = 12
    elif len(parts) == 2:
        imei, service_id_str = parts
        try:
            service_id = int(service_id_str)
        except ValueError:
            return None, None
    else:
        return None, None

    if not is_valid_imei(imei):
        return None, None

    return imei, service_id


async def handle_imei(message: types.Message):
    text = message.text.strip()
    imei, service_id = parse_imei_and_service(text)
    if imei is None:
        await message.answer(
            "Неверный формат. Введите IMEI (15 цифр) и serviceId.\n"
            "Например:\n"
            "   353272491542872 12\n"
            "или\n"
            "   353272491542872 15"
        )
        return

    await message.answer("Проверяю IMEI, пожалуйста, подождите...")

    try:
        result = await check_imei(imei, service_id)
    except Exception as e:
        await message.answer(f"Ошибка при проверке IMEI: {str(e)}")
        return

    if "error" in result:
        detail = result.get("detail", "")
        await message.answer(f"Ошибка при проверке IMEI: {result['error']} {detail}")
    else:
        properties = result.get("properties", {})
        response_lines = [
            f"IMEI: {properties.get('imei', 'N/A')}",
            f"MEID: {properties.get('meid', 'N/A')}",
            f"Serial: {properties.get('serial', 'N/A')}",
            f"Warranty Status: {properties.get('warrantyStatus', 'N/A')}",
            f"Sim Lock: {'Yes' if properties.get('simLock') else 'No'}",
            f"GSMA Blacklisted: {'Yes' if properties.get('gsmaBlacklisted') else 'No'}",
        ]
        formatted_result = "\n".join(response_lines)
        await message.answer(f"Результат проверки IMEI:\n{formatted_result}")


def register_imei_handler(dp: Dispatcher):
    dp.message.register(
        handle_imei,
        lambda message: (
            message.content_type == types.ContentType.TEXT
            and message.text
            and (
                len(message.text.strip().split()) == 1
                or len(message.text.strip().split()) == 2
            )
        ),
    )
