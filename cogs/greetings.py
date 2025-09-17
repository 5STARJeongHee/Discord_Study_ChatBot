from config import properties
from discord.ext import commands
import discord
class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

   # 서버 입장 환영
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(properties.NORMAL_CHANNEL_ID)
        if channel:
            await channel.send(f"👋 반갑습니다~ {member.mention} 님")

    # 온라인 상태 변경 감지
    @commands.Cog.listener()
    async def on_presence_update(self, before, after):
        if before.status != discord.Status.online and after.status == discord.Status.online:
            print(f"{after.display_name} is now online!")
            channel = self.bot.get_channel(properties.NORMAL_CHANNEL_ID)
            if channel:
                await channel.send(f"👋 안녕하세요 {before.display_name}님 오늘은 어떤 공부를 하시겠나요? \n /view_goal 을 통해서 공부할 대상을 선택해주세요")

async def setup(bot):
    await bot.add_cog(Greetings(bot))