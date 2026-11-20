from aiogram.types import Update
from fastapi import FastAPI, Request

from main import bot, dp


app = FastAPI()


@app.get("/")
async def health():
    return {"ok": True}


@app.post("/api")
async def telegram_webhook(request: Request):
    payload = await request.json()
    update = Update.model_validate(payload)
    await dp.feed_update(bot, update)
    return {"ok": True}
