import aiohttp
from app.app.core.config import settings


async def check_imei(imei: str, service_id: int) -> dict:
    url = f"{settings.IMEICHECK_API_URL}/v1/checks"
    headers = {
        "Authorization": f"Bearer {settings.IMEICHECK_API_TOKEN}",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    }
    payload = {"deviceId": imei, "serviceId": service_id}

    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(url, json=payload, headers=headers) as response:
                if 200 <= response.status < 300:
                    return await response.json()
                else:
                    return {
                        "error": f"HTTP error: {response.status}",
                        "detail": await response.text(),
                    }
        except aiohttp.ClientError as e:
            return {"error": f"Client error: {str(e)}"}
        except Exception as e:
            return {"error": f"Unexpected error: {str(e)}"}
