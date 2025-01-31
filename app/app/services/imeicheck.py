import aiohttp
from app.app.core.config import settings


async def check_imei(imei: str) -> dict:
    url = f"{settings.IMEICHECK_API_URL}/v1/checks"
    headers = {
        "Authorization": f"Bearer {settings.IMEICHECK_API_TOKEN}",
        "Content-Type": "application/json",
    }
    payload = {
        "imei": imei,
        "serviceId": 1,
    }

    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(url, json=payload, headers=headers) as response:
                if response.status == 200:
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
