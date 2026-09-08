import logging

from fastapi import FastAPI, Request, HTTPException
from telebot import types

from bot import bot


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
async def root():
    return {
        "status": "ok",
        "message": "Telegram bot is running"
    }


@app.post("/api/webhook")
async def webhook(request: Request):
    try:
        data = await request.json()

        logger.info("Получен Telegram update")

        update = types.Update.de_json(data)

        bot.process_new_updates([update])

        logger.info("Update обработан")

        return {
            "ok": True
        }

    except Exception:
        logger.exception("Ошибка обработки webhook")

        raise HTTPException(
            status_code=500,
            detail="Webhook processing failed"
        )