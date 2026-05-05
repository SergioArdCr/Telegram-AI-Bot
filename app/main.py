from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from telegram.ext import ApplicationBuilder, MessageHandler, filters
from app.bot.handlers import handle_message
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

bot_app = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global bot_app
    bot_app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    bot_app.add_handler(MessageHandler(filters.TEXT, handle_message))
    await bot_app.initialize()
    await bot_app.start()

    if WEBHOOK_URL:
        await bot_app.bot.set_webhook(f"{WEBHOOK_URL}/webhook")
    else:
        await bot_app.updater.start_polling()

    yield

    if WEBHOOK_URL:
        await bot_app.bot.delete_webhook()
    else:
        await bot_app.updater.stop()

    await bot_app.stop()
    await bot_app.shutdown()

app = FastAPI(lifespan=lifespan)

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    from telegram import Update
    update = Update.de_json(data, bot_app.bot)
    await bot_app.process_update(update)
    return {"ok": True}

@app.get("/health")
def health():
    return {"status": "ok"}