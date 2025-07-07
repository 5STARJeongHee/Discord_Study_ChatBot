from discord import app_commands, Interaction

@app_commands.command(name="hello", description="인사하는 명령어")
async def hello_command(interaction: Interaction):
    await interaction.response.send_message(f"안녕하세요, {interaction.user.mention}!")

async def setup(bot):
    bot.tree.add_command(hello_command)
