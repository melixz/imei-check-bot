from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    TELEGRAM_BOT_TOKEN: str = ""
    ALLOWED_USER_IDS: str = ""
    API_AUTH_TOKEN: str = ""
    IMEICHECK_API_TOKEN: str = ""
    IMEICHECK_API_URL: str = ""

    class Config:
        env_file = ".env"

    @property
    def allowed_user_ids_list(self) -> list[int]:
        if self.ALLOWED_USER_IDS:
            return [
                int(uid.strip())
                for uid in self.ALLOWED_USER_IDS.split(",")
                if uid.strip().isdigit()
            ]
        return []


settings = Settings()
