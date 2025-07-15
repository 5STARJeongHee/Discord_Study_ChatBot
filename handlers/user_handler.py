from discord import Interaction, ui
from api.user_api import register_user

async def handle_register_user(interaction: Interaction, button: ui.Button):
    print("[INFO] 사용자 등록 요청")
    print(f"[INFO] /register_user 명령 실행 by {interaction.user.name}")
    payload = {
        "id": interaction.user.id,
        "name": interaction.user.name
    }
    response = await register_user(payload)
    if response.status_code == 200:
        print("[INFO] 사용자 등록 성공")
        await interaction.response.send_message("사용자 등록이 완료되었습니다.", ephemeral=True)
    else:
        print(f"[ERROR] 사용자 등록 실패: {response.status_code} - {response.text}")
        await interaction.response.send_message("사용자 등록에 실패했습니다.", ephemeral=True)
