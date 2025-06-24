from discord import ui, Interaction, ButtonStyle
from ui.goal_form import GoalFormModal
from ui.goal_edit_form import GoalEditModal

class HelpButtonView(ui.View):
    # discord, ui view를 상속하여 
    # 데코레이터 방식으로 ui 아이템들을 등록
    @ui.button(label="목표 등록", custom_id="register_goal", style=ButtonStyle.green)
    async def register_goal(self, interaction: Interaction, button: ui.Button):
        print("[INFO] 사용자 목표 등록 요청")
        await interaction.response.send_modal(GoalFormModal(title="목표 등록"))

    @ui.button(label="목표 수정", custom_id="edit_goal", style=ButtonStyle.blurple)
    async def edit_goal(self, interaction: Interaction, button: ui.Button):
        print("[INFO] 사용자 목표 수정 요청")
        goal_id = "example-goal-id"
        default_values = {
            "name": "파이썬 공부",
            "category": "개발",
            "total_goal": "100",
            "unit": "시간"
        }
        await interaction.response.send_modal(GoalEditModal(goal_id, default_values))

    @ui.button(label="목표 조회", custom_id="view_goal", style=ButtonStyle.gray)
    async def view_goal(self, interaction: Interaction, button: ui.Button):
        print("[INFO] 사용자 목표 조회 요청")
        await interaction.response.send_message("🔍 등록된 목표를 조회합니다. (샘플 응답)", ephemeral=True)

    @ui.button(label="목표 삭제", custom_id="delete_goal", style=ButtonStyle.red)
    async def delete_goal(self, interaction: Interaction, button: ui.Button):
        print("[INFO] 사용자 목표 삭제 요청")
        await interaction.response.send_message("🗑️ 목표 삭제 요청을 받았습니다. (샘플 응답)", ephemeral=True)

    @ui.button(label="학습 시작", custom_id="start_goal", style=ButtonStyle.success)
    async def start_goal(self, interaction: Interaction, button: ui.Button):
        print("[INFO] 학습 시작 요청")
        await interaction.response.send_message("🚀 학습을 시작합니다. (샘플 응답)", ephemeral=True)

    @ui.button(label="학습 종료", custom_id="stop_goal", style=ButtonStyle.danger)
    async def stop_goal(self, interaction: Interaction, button: ui.Button):
        print("[INFO] 학습 종료 요청")
        await interaction.response.send_message("🛑 학습을 종료합니다. (샘플 응답)", ephemeral=True)
