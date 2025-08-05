# utils/http_discord.py
import os
import aiohttp
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

headers = {
    "Authorization": f"Bot {DISCORD_TOKEN}",
    "Content-Type": "application/json"
}

async def send_v2_section_message(channel_id: str, components: list, content: str = ""):
    message_data = {
        "content": content,
        "flags": 1 << 15,  # IS_COMPONENTS_V2
        "components": components
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(
            f"https://discord.com/api/v10/channels/{channel_id}/messages",
            headers=headers,
            json=message_data
        ) as resp:
            data = await resp.json()
            if resp.status != 200:
                print(f"[ERROR] V2 메시지 전송 실패: {data}")
            else:
                print(f"[INFO] V2 메시지 전송 성공: {data}")
            return data
