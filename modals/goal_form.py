# ui/goal_form.py
from discord import ui, Interaction
from api.goal_api import register_goal_api, edit_goal_api

class GoalFormModal(ui.Modal):
    def __init__(self, title="목표 설정"):
        super().__init__(title=title)
        self.name = ui.TextInput(label="목표 이름")
        self.category = ui.TextInput(label="카테고리")
        self.total_goal = ui.TextInput(label="총 목표 수치")
        self.current_progress = ui.TextInput(label="현재 진행 수치", required=False)
        self.unit = ui.TextInput(label="단위")

        self.add_item(self.name)
        self.add_item(self.category)
        self.add_item(self.total_goal)
        self.add_item(self.unit)

    async def on_submit(self, interaction: Interaction):

        payload = {
            "user": interaction.user.id,
            "name": self.name.value,
            "category": self.category.value,
            "total_goal": self.total_goal.value,
            "current_progress": self.current_progress.value or 0,
            "unit": self.unit.value
        }
        
        response = await register_goal_api(payload)

        if response.status_code == 200:
            print("[INFO] 목표가 성공적으로 저장되었습니다.")
            print(f"[INFO] 저장된 목표: {payload}")
            await interaction.response.send_message("목표가 저장되었습니다.", ephemeral=True)
        else:
            print(f"[ERROR] 목표 저장 실패: {response.status_code} - {response.text}")
            await interaction.response.send_message("목표 저장 실패!", ephemeral=True)


class GoalEditModal(ui.Modal):
    def __init__(self, goal_id: str, default_values: dict):
        super().__init__(title="목표 수정")
        self.goal_id = goal_id
        
        self.name = ui.TextInput(label="목표 이름", default=default_values.get("name", ""))
        self.category = ui.TextInput(label="카테고리", default=default_values.get("category", ""))
        self.total_goal = ui.TextInput(label="총 목표 수치", default=default_values.get("total_goal", ""))
        self.current_progress = ui.TextInput(label="현재 진행 수치", required=False)
        self.unit = ui.TextInput(label="단위", default=default_values.get("unit", ""))

        self.add_item(self.name)
        self.add_item(self.category)
        self.add_item(self.total_goal)
        self.add_item(self.current_progress)
        self.add_item(self.unit)

    async def on_submit(self, interaction: Interaction):
        payload = {
            "name": self.name.value,
            "category": self.category.value,
            "total_goal": self.total_goal.value,
            "unit": self.unit.value
        }
        response = edit_goal_api(self.goal_id, payload)

        if response.status_code == 200:
            print("[INFO] 목표가 성공적으로 수정되었습니다.")
            print(f"[INFO] 목표 ID: {self.goal_id}, 수정된 값: {payload}")
            await interaction.response.send_message("목표가 성공적으로 수정되었습니다!", ephemeral=True)
        else:
            print(f"[ERROR] 목표 수정 실패: {response.status_code} - {response.text}")
            await interaction.response.send_message("목표 수정에 실패했습니다.", ephemeral=True)
