from discord import ui, Interaction, ButtonStyle
from handlers.help_handler import handle_register_goal, handle_edit_goal, handle_view_goals, handle_delete_goal, handle_start_goal, handle_stop_goal

class HelpButtonView(ui.View):
    
    # discord, ui view를 상속하여 
    # 데코레이터 방식으로 ui 아이템들을 등록
    @ui.button(label="목표 등록", custom_id="register_goal", style=ButtonStyle.green, row=0)
    async def register_goal(self, interaction: Interaction, button: ui.Button):
        await handle_register_goal(interaction, button)

    @ui.button(label="목표 수정", custom_id="edit_goal", style=ButtonStyle.blurple, row=0)
    async def edit_goal(self, interaction: Interaction, button: ui.Button):
        await handle_edit_goal(interaction, button)

    @ui.button(label="목표 목록 조회", custom_id="view_goal", style=ButtonStyle.gray, row=2)
    async def view_goal(self, interaction: Interaction, button: ui.Button):
        await handle_view_goals(interaction, button)

    @ui.button(label="목표 삭제", custom_id="delete_goal", style=ButtonStyle.red, row=2)
    async def delete_goal(self, interaction: Interaction, button: ui.Button):
        await handle_delete_goal(interaction, button)

    @ui.button(label="학습 시작", custom_id="start_goal", style=ButtonStyle.success, row=3)
    async def start_goal(self, interaction: Interaction, button: ui.Button):
        await handle_start_goal(interaction, button)

    @ui.button(label="학습 종료", custom_id="stop_goal", style=ButtonStyle.danger, row=3)
    async def stop_goal(self, interaction: Interaction, button: ui.Button):
        await handle_stop_goal(interaction, button)