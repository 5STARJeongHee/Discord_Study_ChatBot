from discord import ui, Interaction, ButtonStyle
from handlers.user_handler import handle_register_user


class RegisterUserButtonView(ui.View):

    @ui.button(label="현재 사용자 등록", custom_id="register_user", style=ButtonStyle.green)
    async def register_user(self, interaction: Interaction, button: ui.Button):
        await handle_register_user(interaction, button)