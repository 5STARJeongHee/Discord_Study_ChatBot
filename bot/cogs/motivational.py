import discord
from discord.ext import commands

class Motivational(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="motivate")
    async def motivate(self, ctx):
        await ctx.send("💪 You can do it! Stay focused!")

# ⬇️ Cog 등록용 엔트리포인트 필수
async def setup(bot):
    await bot.add_cog(Motivational(bot))
    print("✅ Motivational Cog loaded")
