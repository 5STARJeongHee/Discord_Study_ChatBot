# events/user_tracking.py
import requests
import discord
import os
from dotenv import load_dotenv

load_dotenv()
channel_id = os.getenv("NORMAL_CHANNEL_ID")
async def on_member_join(member: discord.Member):
    
    user_info = {
        "discord_id": str(member.id),
        "nickname": member.display_name
    }
    print(f"✅ 새 유저 가입: {member.display_name}")
    channel = member.guild.system_channel  # 시스템 메시지 채널이 있다면 여기에
    if channel:
        await channel.send(f"🎉 {member.mention}님, 서버에 오신 걸 환영합니다!")
    #requests.post("https://your.api/users", json=user_info)

async def on_presence_update(before: discord.Member, after: discord.Member):
    channel_object = after.guild.get_channel(int(channel_id))
    if channel_object is not None and channel_object.type == discord.ChannelType.text:
        if after.status == 'online':
            await channel_object.send("안녕하세요" + after.display_name + " 님 오늘은 어떤 목표를 달성하실 건가요? \n " +
                                                                 "/help 를 통해 명령해주세요" )
    else: 
        print("channel is None")
    
    if before.status != after.status and after.status == discord.Status.online:
        print(f"{after.display_name} is online")
        # TODO: 유저 목표 조회 후 알림 또는 학습 시작 안내
