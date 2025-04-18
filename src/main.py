from fastapi import FastAPI
from tap_to_earn import TapToEarn

app = FastAPI()

users = {}

@app.get("/user/{user_id}")
async def get_user(user_id: int):
    if user_id not in users:
        users[user_id] = TapToEarn(user_id)
    user = users[user_id]
    return {"user_id": user.user_id, "coins": user.coins, "energy": user.energy}

@app.post("/tap/{user_id}")
async def tap(user_id: int):
    if user_id not in users:
        users[user_id] = TapToEarn(user_id)
    user = users[user_id]
    coins = user.tap()
    success = coins > 0
    return {"success": success, "coins": user.coins, "energy": user.energy}
