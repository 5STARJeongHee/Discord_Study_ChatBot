from discord import app_commands, Interaction
from views.user_view import RegisterUserButtonView


@app_commands.command(name="register_user", description="현재 사용자 등록")
async def register_user_command(interaction: Interaction):
    print(f"[INFO] /register_user 명령 실행 by {interaction.user.name}")
    view = RegisterUserButtonView()
    await interaction.response.send_message("🧾 사용자 등록 버튼", view=view, ephemeral=True)

async def setup(bot):
    bot.tree.add_command(register_user_command)