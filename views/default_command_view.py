from discord import ui, Interaction, ButtonStyle
from handlers.goal_handler import handle_register_goal, handle_edit_goal, handle_view_goal, handle_delete_goal, handle_start_goal, handle_stop_goal


class RegisterGoalButtonView(ui.View):

    @ui.button(label="목표 등록", custom_id="register_goal", style=ButtonStyle.green)
    async def register_goal(self, interaction: Interaction, button: ui.Button):
        await handle_register_goal(interaction, button)

class EditGoalButtonView(ui.View):

    @ui.button(label="목표 수정", custom_id="edit_goal", style=ButtonStyle.blurple)
    async def edit_goal(self, interaction: Interaction, button: ui.Button):
        await handle_edit_goal(interaction, button)

class ViewGoalButtonView(ui.View):

    @ui.button(label="목표 조회", custom_id="view_goal", style=ButtonStyle.gray)
    async def view_goal(self, interaction: Interaction, button: ui.Button):
        await handle_view_goal(interaction, button)

class DeleteGoalButtonView(ui.View):

    @ui.button(label="목표 삭제", custom_id="delete_goal", style=ButtonStyle.red)
    async def delete_goal(self, interaction: Interaction, button: ui.Button):
        await handle_delete_goal(interaction, button)

class StartGoalButtonView(ui.View):

    @ui.button(label="학습 시작", custom_id="start_goal", style=ButtonStyle.success)
    async def start_goal(self, interaction: Interaction, button: ui.Button):
        await handle_start_goal(interaction, button)

class StopGoalButtonView(ui.View):

    @ui.button(label="학습 종료", custom_id="stop_goal", style=ButtonStyle.danger)
    async def stop_goal(self, interaction: Interaction, button: ui.Button):
        await handle_stop_goal(interaction, button)