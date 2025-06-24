# ui/goal_form.py
from discord import ui, Interaction
import requests

class GoalFormModal(ui.Modal):
    def __init__(self, title="목표 설정"):
        super().__init__(title=title)
        self.name = ui.TextInput(label="목표 이름")
        self.category = ui.TextInput(label="카테고리")
        self.total_goal = ui.TextInput(label="총 목표 수치")
        self.unit = ui.TextInput(label="단위")

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
        # TODO: 실제 API 주소로 교체
        response = requests.post("https://your.api/goal", json=payload)

        if response.status_code == 200:
            await interaction.response.send_message("목표가 저장되었습니다.", ephemeral=True)
        else:
            await interaction.response.send_message("목표 저장 실패!", ephemeral=True)
