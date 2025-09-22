# config.py
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))
API_BASE_URL = os.getenv("API_BASE_URL")
NORMAL_CHANNEL_ID = int(os.getenv("NORMAL_CHANNEL_ID"))
SERVER_URL = os.getenv("SERVER_URL", "http://localhost:8000")
