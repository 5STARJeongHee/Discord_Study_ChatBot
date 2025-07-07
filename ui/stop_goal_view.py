from discord import ui, Interaction, ButtonStyle
from ui.goal_form import GoalFormModal
from ui.goal_edit_form import GoalEditModal

class StopGoalButtonView(ui.View):
    # discord, ui view를 상속하여
    # 데코레이터 방식으로 ui 아이템들을 등록

    @ui.button(label="학습 종료", custom_id="stop_goal", style=ButtonStyle.danger)
    async def stop_goal(self, interaction: Interaction, button: ui.Button):
        print("[INFO] 학습 종료 요청")
        await interaction.response.send_message("🛑 학습을 종료합니다. (샘플 응답)", ephemeral=True)
