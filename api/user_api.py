import httpx
from config.properties import SERVER_URL

async def register_user(payload: dict) -> httpx.Response:
    url = f"{SERVER_URL}/api/user/join"
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload)
    return response