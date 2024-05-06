import types
from aiogram.filters.command import Command
from config import token
from aiogram import *
import asyncio
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from info import plot_thingspeak_temperature, plot_thingspeak_humidity, plot_thingspeak_light, plot_thingspeak_noise, plot_thingspeak_gases
import datetime
bot = Bot(token=token)

# Создаем диспетчер для обработки команд и сообщений бота
dp = Dispatcher()



@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Температура")],
        [types.KeyboardButton(text="Влажность")],
        [types.KeyboardButton(text="Освещенность")],
        [types.KeyboardButton(text="Уровень шума")],
        [types.KeyboardButton(text="Уровень газов")],

    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("""Привет, солнце <3
Тыкни на кнопку и ты получишь состояние твоей окружающей среды за последние 8 часов""", reply_markup=keyboard)


@dp.message(F.text == 'Температура')
async def send_temperature_plot(message: types.Message):
    plot_thingspeak_temperature()
    await message.answer_photo(
        types.FSInputFile(path='temperature_plot.jpg'), caption="График температуры"
    )


@dp.message(F.text == 'Влажность')
async def send_humidity_plot(message: types.Message):
    plot_thingspeak_humidity()
    await message.answer_photo(
        types.FSInputFile(path='humidity_plot.jpg'), caption="График влажности"
    )



@dp.message(F.text == 'Освещенность')
async def send_light_plot(message: types.Message):
    plot_thingspeak_light()
    await message.answer_photo(
        types.FSInputFile(path='light_plot.jpg'), caption="График освещенности"
    )

@dp.message(F.text == 'Уровень шума')
async def send_noise_plot(message: types.Message):
    plot_thingspeak_noise()
    await message.answer_photo(
        types.FSInputFile(path='noise_plot.jpg'), caption="График уровня шума"
    )


@dp.message(F.text == 'Уровень газов')
async def send_noise_plot(message: types.Message):
    plot_thingspeak_gases()
    await message.answer_photo(
        types.FSInputFile(path='gases_plot.jpg'), caption="График уровня газов"
    )








async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())  # tg_bot