# events/user_tracking.py
import requests
import discord

async def on_member_join(member: discord.Member):
    user_info = {
        "discord_id": str(member.id),
        "nickname": member.display_name
    }
    requests.post("https://your.api/users", json=user_info)

async def on_presence_update(before: discord.Member, after: discord.Member):
    if before.status != after.status and after.status == discord.Status.online:
        print(f"{after.display_name} is online")
        # TODO: 유저 목표 조회 후 알림 또는 학습 시작 안내
