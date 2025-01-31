from aiogram import types, Dispatcher, BaseMiddleware
from aiogram.dispatcher.event.bases import CancelHandler

from app.app.core.config import settings


class WhiteListMiddleware(BaseMiddleware):
    def __init__(self, allowed_user_ids: list[int]):
        super().__init__()
        self.allowed_user_ids = allowed_user_ids

    async def __call__(self, handler, event: types.TelegramObject, data: dict) -> any:
        if isinstance(event, types.Message):
            user_id = event.from_user.id
            if user_id not in self.allowed_user_ids:
                await event.answer("Извините, у вас нет доступа к этому боту.")
                raise CancelHandler()
        return await handler(event, data)


def setup_middlewares(dp: Dispatcher):
    allowed_ids = [
        int(uid.strip())
        for uid in settings.ALLOWED_USER_IDS.split(",")
        if uid.strip().isdigit()
    ]
    dp.message.middleware(WhiteListMiddleware(allowed_user_ids=allowed_ids))
