from discord import ui, Interaction, ButtonStyle
from ui.goal_form import GoalFormModal
from ui.goal_edit_form import GoalEditModal

class EditGoalButtonView(ui.View):
    # discord, ui view를 상속하여
    # 데코레이터 방식으로 ui 아이템들을 등록

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

