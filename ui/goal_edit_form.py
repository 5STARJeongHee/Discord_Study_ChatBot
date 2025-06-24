# ui/goal_edit_form.py
from discord import ui, Interaction
import requests

class GoalEditModal(ui.Modal):
    def __init__(self, goal_id: str, default_values: dict):
        super().__init__(title="목표 수정")
        self.goal_id = goal_id
        
        self.name = ui.TextInput(label="목표 이름", default=default_values.get("name", ""))
        self.category = ui.TextInput(label="카테고리", default=default_values.get("category", ""))
        self.total_goal = ui.TextInput(label="총 목표 수치", default=default_values.get("total_goal", ""))
        self.unit = ui.TextInput(label="단위", default=default_values.get("unit", ""))

        self.add_item(self.name)
        self.add_item(self.category)
        self.add_item(self.total_goal)
        self.add_item(self.unit)

    async def on_submit(self, interaction: Interaction):
        payload = {
            "name": self.name.value,
            "category": self.category.value,
            "total_goal": self.total_goal.value,
            "unit": self.unit.value
        }
        response = requests.put(f"https://your.api/goal/{self.goal_id}", json=payload)

        if response.status_code == 200:
            await interaction.response.send_message("목표가 성공적으로 수정되었습니다!", ephemeral=True)
        else:
            await interaction.response.send_message("목표 수정에 실패했습니다.", ephemeral=True)
