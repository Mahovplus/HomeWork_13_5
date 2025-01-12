from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api = "8142808636:AAEy6hDEBYEY55uEy0vPiSE5o8rfcw6rSi4"
bot = Bot(token = api)
dp = Dispatcher(bot, storage= MemoryStorage())

kb = ReplyKeyboardMarkup()
button = KeyboardButton(text="Информация")
button_2 = KeyboardButton(text='Начало')
kb.add(button)
kb.add(button_2)
# kb.row kb.insert

@dp.message_handler(commands='start')
async def start(message):
    await message.answer("Привет!", reply_markup=kb)

@dp.message_handler(text="Начало")
async def inform(message):
    await message.answer("Ура, мы с вами умеем делать информацию о боте.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
