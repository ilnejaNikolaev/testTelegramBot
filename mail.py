from aiogram import Dispatcher, executor, types, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
import asyncio

api ='8632306485:AAECgOimcdFFlVElc6wF5hdomxRu08BPnNI'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text='Информация')
button2 = KeyboardButton(text='Начало')
kb.add(button)
kb.add(button2)
@dp.message_handler(commands=['start'])
async def send_welcome(message):
    print(f"Получена команда старт от {message.from_user.username}")
    await message.answer('Привет',reply_markup=kb)

@dp.message_handler(text= 'Иформация')
async def inform(message):
    await message.answer('Инфомация о боте')




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)