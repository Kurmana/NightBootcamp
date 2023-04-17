import logging
import requests
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

import random

markup = ReplyKeyboardMarkup()
markup.add(KeyboardButton('/start'), KeyboardButton('/счет'))


API_TOKEN = '6065351917:AAGd-NpZerKU4rN-iR9teR6RBGLlvVZW6ls'
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

choises = ['Камень', 'Ножницы', 'Бумага']

messagemarkup = InlineKeyboardMarkup()
messagemarkup.add(InlineKeyboardButton('🗿Камень', callback_data='Камень'), InlineKeyboardButton('✂️Ножницы', callback_data='Ножницы'), InlineKeyboardButton('📄Бумага', callback_data='Бумага'))

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer('Начинаем игру камень, ножницы, бумага', reply_markup=markup)
    await message.answer('Выберите одну из них', reply_markup=messagemarkup)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer('Прости ничего не умею')


@dp.callback_query_handler()
async def calldatadeffunc(call: types.callback_query):
    choise = random.choice(choises)
    if choise == call.data:
        await bot.send_message(chat_id=call.from_user.id, text='ничья')
    elif choise == 'Бумага' and call.data == 'Камень' or choise == 'Камень' and call.data == 'Ножницы' or choise == 'Ножницы' and call.data == 'Бумага':
        await bot.send_message(chat_id=call.from_user.id, text=f'Я выбрал {choise}\nВы проиграли 😢😢')
    elif call.data == 'Бумага' and choise == 'Камень' or call.data == 'Камень' and choise == 'Ножницы' or call.data == 'Ножницы' and choise == 'Бумага':
        await bot.send_message(chat_id=call.from_user.id, text=f'Я выбрал {choise}\nВы выйграли 🥳🥳')
    await bot.send_message(chat_id=call.from_user.id, text='Выберите одну из них', reply_markup=messagemarkup)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)