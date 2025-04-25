from fastapi import FastAPI, Request
from bot import bot, WEBHOOK_URL
import uvicorn

app = FastAPI()

@app.on_event("startup")
async def startup():
    await bot.set_webhook(WEBHOOK_URL)

@app.post("/webhook")
async def webhook(request: Request):
    from telegram import Update
    update = Update.de_json(await request.json(), bot)
    async with bot:
        await bot.process_update(update)
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)