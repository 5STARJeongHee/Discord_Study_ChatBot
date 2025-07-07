from discord import ui, Interaction, ButtonStyle
from ui.goal_form import GoalFormModal
from ui.goal_edit_form import GoalEditModal

class DeleteGoalButtonView(ui.View):
    # discord, ui view를 상속하여
    # 데코레이터 방식으로 ui 아이템들을 등록

    @ui.button(label="목표 삭제", custom_id="delete_goal", style=ButtonStyle.red)
    async def delete_goal(self, interaction: Interaction, button: ui.Button):
        print("[INFO] 사용자 목표 삭제 요청")
        await interaction.response.send_message("🗑️ 목표 삭제 요청을 받았습니다. (샘플 응답)", ephemeral=True)
