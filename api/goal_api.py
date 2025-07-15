import httpx
from config.properties import SERVER_URL

async def register_goal_api(payload: dict) -> httpx.Response:
    url = f"{SERVER_URL}/api/goals/register"
    print(f"[INFO] 목표 등록 API 호출: {url} with payload: {payload}")
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload)
    return response

async def edit_goal_api(goal_id , payload: dict) -> httpx.Response:
    url = f"{SERVER_URL}/api/goals/f{goal_id}"
    print(f"[INFO] 목표 수정 API 호출: {url} with payload: {payload}")
    async with httpx.AsyncClient() as client:
        response = await client.put(url, json=payload)
    return response

async def view_goals_api(user_id: str) -> httpx.Response:
    url = f"{SERVER_URL}/api/goals/list?id={user_id}"
    print(f"[INFO] 목표 목록 조회 API 호출: {url} for user_id: {user_id}")
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response