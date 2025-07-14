from discord import app_commands, Interaction
from views.help_view import HelpButtonView

@app_commands.command(name="help", description="사용 가능한 명령어를 보여줍니다.")
async def help_command(interaction: Interaction):
    print(f"[INFO] /help 명령 실행 by {interaction.user.name}")
    view = HelpButtonView()
    await interaction.response.send_message("🧾 사용 가능한 기능 목록:", view=view, ephemeral=True)

async def setup(bot):
    bot.tree.add_command(help_command)