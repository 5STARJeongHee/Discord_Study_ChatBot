from discord import ui, Interaction, ButtonStyle
from ui.goal_form import GoalFormModal
from ui.goal_edit_form import GoalEditModal

class ViewGoalButtonView(ui.View):
    # discord, ui view를 상속하여
    # 데코레이터 방식으로 ui 아이템들을 등록

    @ui.button(label="목표 조회", custom_id="view_goal", style=ButtonStyle.gray)
    async def view_goal(self, interaction: Interaction, button: ui.Button):
        print("[INFO] 사용자 목표 조회 요청")
        await interaction.response.send_message("🔍 등록된 목표를 조회합니다. (샘플 응답)", ephemeral=True)