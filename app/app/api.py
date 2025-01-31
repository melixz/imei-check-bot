from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.app.schemas.imei import IMEICheckRequest
from app.app.services.imeicheck import check_imei
from app.app.utils.imei_validator import is_valid_imei
from app.app.core.config import settings

app = FastAPI()

security = HTTPBearer()


def verify_api_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    if token != settings.API_AUTH_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token


@app.post("/api/check-imei")
async def api_check_imei(
    request: IMEICheckRequest,
    _: str = Depends(verify_api_token),
):
    if not is_valid_imei(request.imei):
        raise HTTPException(status_code=400, detail="Invalid IMEI")

    try:
        result = await check_imei(request.imei)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error checking IMEI: {str(e)}")

    return result


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
