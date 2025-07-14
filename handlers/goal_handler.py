from discord import Interaction, ui
from modals.goal_form import GoalFormModal
from modals.goal_form import GoalEditModal

async def handle_register_goal(interaction: Interaction, button: ui.Button):
    print("[INFO] 사용자 목표 등록 요청")
    print(f"[INFO] /register_goal 명령 실행 by {interaction.user.name}")
    await interaction.response.send_modal(GoalFormModal(title="목표 등록"))


async def handle_edit_goal(self, interaction: Interaction, button: ui.Button):
    print("[INFO] 사용자 목표 수정 요청")
    print(f"[INFO] /edit_goal 명령 실행 by {interaction.user.name}")
    goal_id = "example-goal-id"
    default_values = {
        "name": "파이썬 공부",
        "category": "개발",
        "total_goal": "100",
        "current_progress": 0,
        "unit": "시간"
    }
    await interaction.response.send_modal(GoalEditModal(goal_id, default_values))


async def handle_view_goal(self, interaction: Interaction, button: ui.Button):
    print("[INFO] 사용자 목표 조회 요청")
    print(f"[INFO] /view_goal 명령 실행 by {interaction.user.name}")
    await interaction.response.send_message("🔍 등록된 목표를 조회합니다. (샘플 응답)", ephemeral=True)


async def handle_delete_goal(self, interaction: Interaction, button: ui.Button):
    print("[INFO] 사용자 목표 삭제 요청")
    print(f"[INFO] /delete_goal 명령 실행 by {interaction.user.name}")
    await interaction.response.send_message("🗑️ 목표 삭제 요청을 받았습니다. (샘플 응답)", ephemeral=True)


async def handle_start_goal(self, interaction: Interaction, button: ui.Button):
    print("[INFO] 학습 시작 요청")
    print(f"[INFO] /start_goal 명령 실행 by {interaction.user.name}")
    await interaction.response.send_message("🚀 학습을 시작합니다. (샘플 응답)", ephemeral=True)


async def handle_stop_goal(self, interaction: Interaction, button: ui.Button):
    print("[INFO] 학습 종료 요청")
    print(f"[INFO] /stop_goal 명령 실행 by {interaction.user.name}")
    await interaction.response.send_message("🛑 학습을 종료합니다. (샘플 응답)", ephemeral=True)