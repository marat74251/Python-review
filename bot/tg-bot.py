import logging
from db import *
from parser import *
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

APP_TOKEN = "7548029391:AAH70pGo66ka8oxOobaqSpHSgWUCobMgX4A"

url = 'https://s-b-1.ru/catalog/'
cuted_url = 'https://s-b-1.ru'

bot = Bot(token=APP_TOKEN)

dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
button1 = KeyboardButton("Создать")
button2 = KeyboardButton("Распарсить")
keyboard.add(button1)

@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
    await message.reply("Привет! Я бот для парсинга данных и работы с базой.", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Создать")
async def start_handler(message: types.Message):
    create_table()
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button2 = KeyboardButton("Распарсить")
    keyboard.add(button2)
    await message.reply("База создана", reply_markup=keyboard)

@dp.message_handler(commands="get")
async def get_data_handler(message: types.Message):
    data = get_data()
    if (len(data) < 4096):
        await message.reply(f"Данные из базы: {data}")
    else:
        await message.reply("Данных слишком много")

@dp.message_handler(commands="vget")
async def get_data_handler(message: types.Message):
    data = val_get()
    if (len(data) < 4096):
        await message.reply(f"Данные из базы: {data}")
    else:
        await message.reply("Данных слишком много")

@dp.message_handler(lambda message: message.text == "Распарсить")
async def parse_site_handler(message: types.Message):
    url = 'https://s-b-1.ru/catalog/'
    data = exe_fun_heads(url)
    if data:
        save_data_for_head(data)
        if (len(data) < 4096):
            await message.reply(f"Найденные данные: {data}")
        else:
            await message.reply("Данных слишком много")
    else:
        await message.reply("Не удалось получить данные с сайта.")   

@dp.message_handler(commands="clear")
async def start_handler(message: types.Message):
    delete_data()
    await message.reply("Таблица очищениа")

if __name__ == "__main__":
    executor.start_polling(dp)