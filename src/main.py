from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tap_to_earn import TapToEarn

app = FastAPI()
tap_users = {}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://dubai-city-bot.vercel.app"],  # Vercel URL keyin yangilanadi
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/tap/{user_id}")
async def tap(user_id: int):
    if user_id not in tap_users:
        tap_users[user_id] = TapToEarn(user_id)
    coins = tap_users[user_id].tap()
    return {"success": coins > 0, "coins": coins, "energy": tap_users[user_id].energy}
