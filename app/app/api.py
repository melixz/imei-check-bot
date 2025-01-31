from fastapi import FastAPI, HTTPException
from app.app.schemas.imei import IMEICheckRequest
from app.app.services.imeicheck import check_imei
from app.app.utils.imei_validator import is_valid_imei
from app.app.core.config import settings

app = FastAPI()


@app.post("/api/check-imei")
async def api_check_imei(request: IMEICheckRequest):
    if request.token != settings.API_AUTH_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid API token")

    if not is_valid_imei(request.imei):
        raise HTTPException(status_code=400, detail="Invalid IMEI")

    result = await check_imei(request.imei)
    return result


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
