from pydantic import BaseModel


class IMEICheckRequest(BaseModel):
    imei: str
    serviceId: int
