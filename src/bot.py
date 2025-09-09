import os
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from core import AvatarAgent
from router import build_router_chain

load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
agent = AvatarAgent()

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привет! Я — голос бренда. Используй /role pr|sales|support и /ask <вопрос>")

@dp.message_handler(commands=["role"])
async def set_role(message: types.Message):
    role = message.get_args()
    agent.set_role(role)
    await message.answer(f"Режим переключён на {role}")

@dp.message_handler(commands=["ask"])
async def ask(message: types.Message):
    question = message.get_args()
    answer = agent.chat(question)
    await message.answer(answer)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
