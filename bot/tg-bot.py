import logging
from db import get_data, save_data, create_table, delete_data, val_get
from parser import fetch_data_from_site
from aiogram import Bot, Dispatcher, executor, types

APP_TOKEN = "7548029391:AAH70pGo66ka8oxOobaqSpHSgWUCobMgX4A"

PATH_TO_LIST = "result/todo-list.csv"

bot = Bot(token=APP_TOKEN)

dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
    await message.reply("Привет! Я бот для парсинга данных и работы с базой.")

@dp.message_handler(commands="create")
async def start_handler(message: types.Message):
    create_table()
    await message.reply("База создана")

@dp.message_handler(commands="get")
async def get_data_handler(message: types.Message):
    data = get_data()
    await message.reply(f"Данные из базы: {data}")

@dp.message_handler(commands="vget")
async def get_data_handler(message: types.Message):
    data = val_get()
    await message.reply(f"Данные из базы: {data}")

@dp.message_handler(commands="parse")
async def parse_site_handler(message: types.Message):
    url = "https://galeontrade.ru/"
    data = fetch_data_from_site(url)
    if data:
        await message.reply(f"Найденные данные: {', '.join(data)}")
        save_data(data)
    else:
        await message.reply("Не удалось получить данные с сайта.")

@dp.message_handler(commands="clear")
async def start_handler(message: types.Message):
    delete_data()
    await message.reply("Таблица очищениа")

if __name__ == "__main__":
    executor.start_polling(dp)