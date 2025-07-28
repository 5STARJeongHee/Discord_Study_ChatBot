from discord import Interaction, ui
from modals.goal_form import GoalFormModal, GoalEditModal, GoalListView
from api.goal_api import view_goals_api

async def handle_register_goal(interaction: Interaction, button: ui.Button):
    print("[INFO] 사용자 목표 등록 요청")
    print(f"[INFO] /register_goal 명령 실행 by {interaction.user.name}")
    await interaction.response.send_message(
        "COMMAND: /register_goal\n\n" \
        "목표 등록 방법\n\n" \
    "1. 목표 이름을 입력합니다.\n" \
    "2. 카테고리를 선택합니다.\n" \
    "3. 총 목표 수치를 입력합니다.\n" \
    "4. 총 목표치를 입력합니다.\n" \
    "5. 단위를 입력합니다(페이지, 개수, 일, 시간).\n" \
    "6. 제출 버튼을 클릭합니다.", ephemeral=True)
    


async def handle_edit_goal( interaction: Interaction, button: ui.Button):
    print("[INFO] 사용자 목표 수정 요청")
    print(f"[INFO] /edit_goal 명령 실행 by {interaction.user.name}")

    await interaction.response.send_message(
        "COMMAND: /edit_goal\n\n" \
        "목표 수정 방법\n\n" \
        "1. 수정할 목표를 선택합니다.\n" \
        "2. 목표 이름을 수정합니다.\n" \
        "3. 카테고리를 수정합니다.\n" \
        "4. 총 목표 수치를 수정합니다.\n" \
        "5.수정 버튼을 클릭합니다.", ephemeral=True)


async def handle_view_goals( interaction: Interaction, button: ui.Button):
    print("[INFO] 사용자 목표 조회 요청")
    print(f"[INFO] /view_goal 명령 실행 by {interaction.user.name}")
    user_id = interaction.user.id

    await interaction.response.send_message(
        "COMMAND: /view_goal\n\n" \
        "목표 조회 방법\n\n" \
        "1. 목표 조회 버튼을 클릭합니다.\n" \
        "2. 등록된 목표 목록이 표시됩니다.\n", ephemeral=True)


async def handle_delete_goal( interaction: Interaction, button: ui.Button):
    print("[INFO] 사용자 목표 삭제 요청")
    print(f"[INFO] /delete_goal 명령 실행 by {interaction.user.name}")
    await interaction.response.send_message(
        "COMMAND: /delete_goal\n\n" \
        "목표 삭제 방법\n\n" \
        "1. 삭제할 목표를 선택합니다.\n" \
        "2. 삭제 버튼을 클릭합니다.\n" \
        "3. 삭제 확인 메시지가 표시됩니다.", ephemeral=True)


async def handle_start_goal( interaction: Interaction, button: ui.Button):
    print("[INFO] 학습 시작 요청")
    print(f"[INFO] /start_goal 명령 실행 by {interaction.user.name}")
    await interaction.response.send_message(
        "COMMAND: /start_goal\n\n" \
        "학습 시작 방법\n\n" \
        "1. 학습 시작 버튼을 클릭합니다.\n" \
        "2. 학습이 시작됩니다.\n", ephemeral=True)


async def handle_stop_goal( interaction: Interaction, button: ui.Button):
    print("[INFO] 학습 종료 요청")
    print(f"[INFO] /stop_goal 명령 실행 by {interaction.user.name}")
    await interaction.response.send_message(
        "COMMAND: /stop_goal\n\n" \
        "학습 종료 방법\n\n" \
        "1. 학습 종료 버튼을 클릭합니다.\n" \
        "2. 학습이 종료됩니다.\n", ephemeral=True)