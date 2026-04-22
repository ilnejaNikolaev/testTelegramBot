from aiogram import Dispatcher, executor, types, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
import asyncio
import logging

from config import *
from keyboards import *
import texts

logging.basicConfig(level=logging.INFO)
bot = Bot(token= API)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(f"Добро пожаловать, {message.from_user.username}"+texts.start,reply_markup = start_kb)

#massage.answer_photo
#.answer_video
#.answer_file  "это тоже можно подгружать в бота"


@dp.message_handler(text= "О нас" )
async def info(message):
    with open('files/4.jpg',"rb") as img:
        await message.answer_photo(img,texts.about,reply_markup = start_kb)

@dp.message_handler(text= "Стоимость")
async def  price(message):
    await message.answer("Что вас интересует?", reply_markup = catalog_kb)

@dp.callback_query_handler(text="medium")
async def buy_m(call):
    await call.message.answer(texts.priceM,reply_markup = buy_kb)
    await call.answer()

@dp.callback_query_handler(text="big")
async def buy_l(call):
    await call.message.answer(texts.priceL,reply_markup = buy_kb)
    await call.answer()

@dp.callback_query_handler(text="mega")
async def buy_xl(call):
    await call.message.answer(texts.priceXL,reply_markup = buy_kb)
    await call.answer()

@dp.callback_query_handler(text="other")
async def buy(call):
    await call.message.answer(texts.other,reply_markup = buy_kb)
    await call.answer()


@dp.callback_query_handler(text="back_to_catalog")
async def back(call):
    await call.message.answer("Что вас интересует?", reply_markup=catalog_kb)
    await call.answer()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)