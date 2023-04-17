import json
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


@dp.message_handler(commands=['счет'])
async def results(message: types.Message):
    with open('database.json', 'r') as f:
        data = json.load(f)
    user = None
    for i in range(len(data['results'])):
        print(data['results'][i]['user'])
        print(message.from_user.id)
        if data['results'][i]['user'] == message.from_user.id:
            user = data['results'][i]
            break
    if user:
        await message.reply(f'Побед - {user["win"]}\n Проиграл - {user["lose"]}\n Ничья - {user["draw"]}')
    else:
        await message.reply('У тебя пока нет счета')


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer('Прости ничего не умею')


@dp.callback_query_handler()
async def calldatadeffunc(call: types.callback_query):
    with open('database.json', 'r') as f:
        data = json.load(f)
    if call.from_user.id in data['users']:
        pass
    else:
        data['users'].append(call.from_user.id)
        data['results'].append({'user': call.from_user.id, 'win': 0, 'lose': 0, 'draw': 0})

    choise = random.choice(choises)
    if choise == call.data:
        for i in range(len(data['results'])):
            if data['results'][i]['user'] == call.from_user.id:
                data['results'][i]['draw'] += 1
                break
        await bot.send_message(chat_id=call.from_user.id, text='ничья')
    elif choise == 'Бумага' and call.data == 'Камень' or choise == 'Камень' and call.data == 'Ножницы' or choise == 'Ножницы' and call.data == 'Бумага':
        for i in range(len(data['results'])):
            if data['results'][i]['user'] == call.from_user.id:
                data['results'][i]['lose'] += 1
                break
        await bot.send_message(chat_id=call.from_user.id, text=f'Я выбрал {choise}\nВы проиграли 😢😢')
    elif call.data == 'Бумага' and choise == 'Камень' or call.data == 'Камень' and choise == 'Ножницы' or call.data == 'Ножницы' and choise == 'Бумага':
        for i in range(len(data['results'])):
            if data['results'][i]['user'] == call.from_user.id:
                data['results'][i]['win'] += 1
                break
        await bot.send_message(chat_id=call.from_user.id, text=f'Я выбрал {choise}\nВы выйграли 🥳🥳')
    with open('database.json', 'w')as f:
        json.dump(data, f)
    await bot.send_message(chat_id=call.from_user.id, text='Выберите одну из них', reply_markup=messagemarkup)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)