import os
import logging

from fastapi import FastAPI, Request, HTTPException
import telebot
from telebot import types

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = os.environ["BOT_TOKEN"]

app = FastAPI()

bot = telebot.TeleBot(TOKEN)