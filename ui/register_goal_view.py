from discord import ui, Interaction, ButtonStyle
from ui.goal_form import GoalFormModal
from ui.goal_edit_form import GoalEditModal

class RegisterGoalButtonView(ui.View):
    # discord, ui view를 상속하여
    # 데코레이터 방식으로 ui 아이템들을 등록
    @ui.button(label="목표 등록", custom_id="register_goal", style=ButtonStyle.green)
    async def register_goal(self, interaction: Interaction, button: ui.Button):
        print("[INFO] 사용자 목표 등록 요청")
        await interaction.response.send_modal(GoalFormModal(title="목표 등록"))
