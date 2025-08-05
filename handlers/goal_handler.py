from discord import Interaction, ui
from views.goal_form import GoalFormModal, GoalEditModal, GoalListEditView
from api.goal_api import view_goals_api
from utils.http_discord import send_v2_section_message

async def handle_register_goal(interaction: Interaction, button: ui.Button):
    print("[INFO] 사용자 목표 등록 요청")
    print(f"[INFO] /register_goal 명령 실행 by {interaction.user.name}")
    await interaction.response.send_modal(GoalFormModal(title="목표 등록"))


async def handle_edit_goal( interaction: Interaction, button: ui.Button):
    print("[INFO] 사용자 목표 수정 요청")
    print(f"[INFO] /edit_goal 명령 실행 by {interaction.user.name}")
    user_id = interaction.user.id
    response = await view_goals_api(user_id)

    if response.status_code == 200:
        goals = response.json()
        if goals:
            # ✅ discord.py 방식
            # view = GoalListEditView(goals, user_id)
            # await interaction.response.send_message("수정할 목표를 선택하세요:", view=view, ephemeral=True)

            # ✅ HTTP API 방식 (V2 사용)
            components = []
            for goal in goals:
                components.append({
                    "type": 9,  # Section
                    "components": [{
                        "type": 0,
                        "text": {
                            "type": "markdown",
                            "content": f"**{goal['name']}**\n{goal['current_progress']}/{goal['total_goal']} {goal['unit']}"
                        }
                    }],
                    "accessory": {
                        "type": 2,
                        "style": 1,
                        "label": "수정",
                        "custom_id": f"edit_goal_{goal['id']}"
                    }
                })

            await interaction.response.send_message("📋 목표 목록을 전송했습니다.", ephemeral=True)
            await send_v2_section_message(interaction.channel_id, components)

        else:
            await interaction.response.send_message("등록된 목표가 없습니다.", ephemeral=True)
    else:
        await interaction.response.send_message("목표 조회 실패!", ephemeral=True)


async def handle_view_goals( interaction: Interaction, button: ui.Button):
    print("[INFO] 사용자 목표 조회 요청")
    print(f"[INFO] /view_goal 명령 실행 by {interaction.user.name}")
    user_id = interaction.user.id
    response = await view_goals_api(user_id)

    if response.status_code == 200:
        goals = response.json()
        if goals:
            # ✅ discord.py 방식
            # view = GoalListEditView(goals, user_id)
            # await interaction.response.send_message("수정할 목표를 선택하세요:", view=view, ephemeral=True)

            # ✅ HTTP API 방식 (V2 사용)
            components = []
            for goal in goals:
                components.append({
                    "type": 9,  # Section
                    "components": [{
                        "type": 0,
                        "text": {
                            "type": "markdown",
                            "content": f"**{goal['name']}**\n{goal['current_progress']}/{goal['total_goal']} {goal['unit']}"
                        }
                    }],
                    "accessory": {
                        "type": 2,
                        "style": 1,
                        "label": "수정",
                        "custom_id": f"edit_goal_{goal['id']}"
                    }
                })

            await interaction.response.send_message("📋 목표 목록을 전송했습니다.", ephemeral=True)
            await send_v2_section_message(interaction.channel_id, components)

        else:
            await interaction.response.send_message("등록된 목표가 없습니다.", ephemeral=True)
    else:
        await interaction.response.send_message("목표 조회 실패!", ephemeral=True)


async def handle_delete_goal( interaction: Interaction, button: ui.Button):
    print("[INFO] 사용자 목표 삭제 요청")
    print(f"[INFO] /delete_goal 명령 실행 by {interaction.user.name}")
    await interaction.response.send_message("🗑️ 목표 삭제 요청을 받았습니다. (샘플 응답)", ephemeral=True)


async def handle_start_goal( interaction: Interaction, button: ui.Button):
    print("[INFO] 학습 시작 요청")
    print(f"[INFO] /start_goal 명령 실행 by {interaction.user.name}")
    await interaction.response.send_message("🚀 학습을 시작합니다. (샘플 응답)", ephemeral=True)


async def handle_stop_goal( interaction: Interaction, button: ui.Button):
    print("[INFO] 학습 종료 요청")
    print(f"[INFO] /stop_goal 명령 실행 by {interaction.user.name}")
    await interaction.response.send_message("🛑 학습을 종료합니다. (샘플 응답)", ephemeral=True)