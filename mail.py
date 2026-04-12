from aiogram import Dispatcher, executor, types, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api ='8632306485:AAEXOBNNKBYa-8wIWZ8kZpE9yQ3pfFjvSCA'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())



@dp.message_handler(text= ['Urban','ff'])
async def urban_message(message):
    print("Urban message")
    await message.answer('Urban message')


@dp.message_handler(commands=['start'])
async def start_message(message):
    print("Start message")
    await message.answer('Рады видеть вас в нашем боте')


@dp.message_handler()
async def all_message(message):
    print("Мы получили сообщение!")
    await message.answer(message.text)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)