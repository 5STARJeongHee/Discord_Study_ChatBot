# bot.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from events import user_tracking
from commands import hi_command, help_commands, default_commands, user_commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = os.getenv("GUILD_ID")
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.presences = True

class MyBot(commands.Bot):
    async def setup_hook(self):
        # 여기서 슬래시 명령어 등록

        await help_commands.setup(self)
        await hi_command.setup(self)
        await default_commands.setup(self)
        await user_commands.setup(self)
        await self.tree.sync()
        print("✅ 슬래시 명령어 동기화 완료")

bot = MyBot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"🤖 봇 준비 완료: {bot.user}")

@bot.event
async def on_member_join(member):
    await user_tracking.on_member_join(member)

@bot.event
async def on_presence_update(before, after):
    await user_tracking.on_presence_update(before, after)

# 실행
bot.run(TOKEN)
