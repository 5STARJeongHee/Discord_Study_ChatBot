import discord
from discord.ext import commands
from config import properties
import asyncio

intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.message_content = True 

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        # bot.run() 전에 비동기 초기화 작업 가능
        await self.load_extension("cogs.greetings")
        await self.load_extension("cogs.motivational")

bot = MyBot()

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")

if __name__ == "__main__":
    bot.run(properties.DISCORD_BOT_TOKEN)