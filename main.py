from fastapi import FastAPI
from starlette.requests import Request
from telegram import Update
from bot import telegram_app

app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, telegram_app.bot)
    await telegram_app.process_update(update)
    return {"ok": True}




