import asyncio 
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup

from config import token


bot = Bot(token=token)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Добро пожаловать в наш Бот {message.from_user.full_name}, чтобы узнать больше о нас нажмите /menu")


@dp.message(F.text =='/menu')
async def menu(message: Message):
    await message.answer("Выберите нужный раздел:", reply_markup=start_keyboard)


start_buttons = [
    [KeyboardButton(text="Новости🌐"), KeyboardButton(text="Курсы валют💲")],
    [KeyboardButton(text="Контактная информация👥"), KeyboardButton(text="Часто задаваемые вопросы (FAQ)🆘")]
]
start_keyboard = ReplyKeyboardMarkup(keyboard=start_buttons, resize_keyboard=True)

@dp.message(F.text =='Новости🌐')
async def news(message: Message):
    await message.answer("""
Минтранс Кыргызстана вводит новые виды сборов.
Кто их будет платить 
Рубль продолжает дешеветь к сому. Остальные валюты немного подорожали
Объем денежных переводов в Кыргызстан в сентябре составил $284,8 миллиона 
""", reply_markup=start_keyboard00 )


@dp.message(F.text =='Курсы валют💲')
async def news(message: Message):
    await message.answer("""
Курсы на сегодняшний день:         
Валюта____покупка_____продажа                        
usd________86.47_______86.86
eur________91.12_______92.09
rub________0.857_______0.876
kzt_________0.1209______0.1828
cny________11.80_______12.55
gbp________109.50______111.00
""", reply_markup=start_keyboard00)
    
@dp.message(F.text =='Контактная информация👥')
async def news(message: Message):
    await message.answer("Наша почта: info@example.com. Телефон: +123456789", reply_markup=start_keyboard001)

@dp.message(F.text =='Часто задаваемые вопросы (FAQ)🆘')
async def sos(message: Message):
    await message.answer("""
/help
/about
/menu
""", reply_markup=start_keyboard00)

@dp.message(F.text =='/about')
async def menu(message: Message):
    await message.answer("Бот создан чтобы помогать пользователям узнавать новости и курсы валют!", reply_markup=start_keyboard00)

@dp.message(F.text =='/help')
async def menu(message: Message):
    await message.answer("""
Новости🌐 - Узнайте новости в мире валюты!
Курсы валют💲 - Мы предоставим вам последние курсы валют.
Контактная информация👥 - Наши контакты
Часто задаваемые вопросы (FAQ)🆘 - Ответы на некотрые ваши вопросы.
""", reply_markup=start_keyboard00)


start_buttons001 = [
    [KeyboardButton(text="INSTAGRAM"), KeyboardButton(text="WHATSAPP")], 
     [KeyboardButton(text="МЕНЮ")],
]
start_keyboard001 = ReplyKeyboardMarkup(keyboard=start_buttons001, resize_keyboard=True)

@dp.message(F.text == "INSTAGRAM") 
async def insta(message: Message):
    await message.answer("https://www.linkedin.com/company/geekskg/")

@dp.message(F.text == "WHATSAPP") 
async def whats(message: Message):
    await message.answer("https://api.whatsapp.com/send/?phone=996507052018&text&type=phone_number&app_absent=0")

@dp.message(F.text == "МЕНЮ") 
async def back_menu(message: Message):
    await message.answer("Выберите нужный раздел:", reply_markup=start_keyboard)

@dp.message(F.text =='Назад')
async def back(message: Message):
    await message.answer("Выберите нужный раздел:",reply_markup=start_keyboard)

start_buttons00 = [
    [KeyboardButton(text="Назад")]
]
start_keyboard00 = ReplyKeyboardMarkup(keyboard=start_buttons00, resize_keyboard=True)



@dp.message()
async def echo(message: Message):
    await message.answer(message.text)


async def main():
    logging.basicConfig(level="INFO")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")


