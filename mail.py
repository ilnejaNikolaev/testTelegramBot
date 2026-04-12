from aiogram import Dispatcher, executor, types, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api ='8632306485:AAECgOimcdFFlVElc6wF5hdomxRu08BPnNI'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    adress = State()

@dp.message_handler(text= "заказать")
async def buy(message):
    await message.answer("Отправь нам свой адрес, пожалуйста")
    await UserState.adress.set()

@dp.message_handler(state= UserState.adress)
async def fsm_handler(message,state):
    await state.update_data(first = message.text)
    data = await state.get_data()
    await message.answer(f"Доставка будет отправленна на {data['first']}")
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)