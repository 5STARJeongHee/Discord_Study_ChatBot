from discord import ui, Interaction, ButtonStyle
from ui.goal_form import GoalFormModal
from ui.goal_edit_form import GoalEditModal

class StartGoalButtonView(ui.View):
    # discord, ui view를 상속하여
    # 데코레이터 방식으로 ui 아이템들을 등록

    @ui.button(label="학습 시작", custom_id="start_goal", style=ButtonStyle.success)
    async def start_goal(self, interaction: Interaction, button: ui.Button):
        print("[INFO] 학습 시작 요청")
        await interaction.response.send_message("🚀 학습을 시작합니다. (샘플 응답)", ephemeral=True)

