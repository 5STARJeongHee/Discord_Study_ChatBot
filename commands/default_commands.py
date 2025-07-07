from discord import app_commands, Interaction
from ui.register_goal_view import RegisterGoalButtonView
from ui.edit_goal_view import EditGoalButtonView
from ui.view_goal_view import ViewGoalButtonView
from ui.delete_goal_view import DeleteGoalButtonView
from ui.start_goal_view import StartGoalButtonView
from ui.stop_goal_view import StopGoalButtonView


@app_commands.command(name="register_goal", description="목표 등록")
async def register_goal_command(interaction: Interaction):
    print(f"[INFO] /register_goal 명령 실행 by {interaction.user.name}")
    view = RegisterGoalButtonView()
    await interaction.response.send_message("🧾 목표 등록 버튼", view=view, ephemeral=True)

@app_commands.command(name="edit_goal", description="목표 수정")
async def edit_goal_command(interaction: Interaction):
    print(f"[INFO] /edit_goal 명령 실행 by {interaction.user.name}")
    view = EditGoalButtonView()
    await interaction.response.send_message("🧾 목표 수정 버튼", view=view, ephemeral=True)

@app_commands.command(name="view_goal", description="목표 조회")
async def view_goal_command(interaction: Interaction):
    print(f"[INFO] /view_goal 명령 실행 by {interaction.user.name}")
    view = ViewGoalButtonView()
    await interaction.response.send_message("🧾 목표 조회 버튼", view=view, ephemeral=True)

@app_commands.command(name="delete_goal", description="목표 삭제")
async def delete_goal_command(interaction: Interaction):
    print(f"[INFO] /delete_goal 명령 실행 by {interaction.user.name}")
    view = DeleteGoalButtonView()
    await interaction.response.send_message("🧾 목표 삭제 버튼", view=view, ephemeral=True)

@app_commands.command(name="start_goal", description="학습 시작")
async def start_goal_command(interaction: Interaction):
    print(f"[INFO] /register 명령 실행 by {interaction.user.name}")
    view = StartGoalButtonView()
    await interaction.response.send_message("🧾 학습 시작 버튼", view=view, ephemeral=True)

@app_commands.command(name="stop_goal", description="학습 종료")
async def stop_goal_command(interaction: Interaction):
    print(f"[INFO] /stop_goal 명령 실행 by {interaction.user.name}")
    view = StopGoalButtonView()
    await interaction.response.send_message("🧾 학습 종료 버튼", view=view, ephemeral=True)


async def setup(bot):
    bot.tree.add_command(register_goal_command)
    bot.tree.add_command(edit_goal_command)
    bot.tree.add_command(view_goal_command)
    bot.tree.add_command(delete_goal_command)
    bot.tree.add_command(start_goal_command)
    bot.tree.add_command(stop_goal_command)