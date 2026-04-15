from aiogram import Dispatcher, executor, types, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
import asyncio

api ='8632306485:AAECgOimcdFFlVElc6wF5hdomxRu08BPnNI'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = InlineKeyboardMarkup()
button = InlineKeyboardButton(text='Информация', callback_data='info')
kb.add(button)

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='info')],
        [
            KeyboardButton(text='shop'),
            KeyboardButton(text='donate'),
        ]
    ],resize_keyboard=True,
)

@dp.message_handler(commands=['start'])
async def send_welcome(message:types.Message):
    await message.answer("Рады вас видеть",reply_markup=start_menu)

@dp.callback_query_handler(text='info')
async def send_info(call):
    await call.message.answer("Информация о боте")
    await call.answer()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)