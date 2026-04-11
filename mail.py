from aiogram import Dispatcher, executor, types, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api ='8632306485:AAEXOBNNKBYa-8wIWZ8kZpE9yQ3pfFjvSCA'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)