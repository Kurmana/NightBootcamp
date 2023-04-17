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

choices = ['камень', 'ножницы', 'бумага']

messagemarkup = InlineKeyboardMarkup()
messagemarkup.add(InlineKeyboardButton('🗿камень', callback_data='камень'), InlineKeyboardButton('✂️ножницы', callback_data='ножницы'), InlineKeyboardButton('📄бумага', callback_data='бумага'))

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer('Давайте поиграем в игру: камень, ножницы, бумага', reply_markup=markup)
    await message.answer('Выберите: камень, ножницы или бумага', reply_markup=messagemarkup)

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
        await message.reply(f'всего побед - {user["win"]}\n всего проигрышей - {user["lose"]}\n ничья - {user["draw"]}')
    else:
        await message.reply('ты еще не играл')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer('не возможно')

@dp.callback_query_handler()
async def calldatadeffunc(call: types.callback_query):
    with open('database.json', 'r') as f:
        data = json.load(f)
    if call.from_user.id in data['users']:
        pass
    else:
        data['users'].append(call.from_user.id)
        data['results'].append({'user': call.from_user.id, 'win': 0, 'lose': 0, 'draw': 0})

    choice = random.choice(choices)
    if choice == call.data:
        for i in range(len(data['results'])):
            if data['results'][i]['user'] == call.from_user.id:
                data['results'][i]['draw'] += 1
                break
        await bot.send_message(chat_id=call.from_user.id, text='ничья🤝')
    elif choice == 'бумага' and call.data == 'камень' or choice == 'камень' and call.data == 'ножницы' or choice == 'ножницы' and call.data == 'бумага':
        for i in range(len(data['results'])):
            if data['results'][i]['user'] == call.from_user.id:
                data['results'][i]['lose'] += 1
                break
        await bot.send_message(chat_id=call.from_user.id, text=f'А я выбрала {choice}\nВы проиграли 😭')
    elif call.data == 'бумага' and choice == 'камень' or call.data == 'камень' and choice == 'ножницы' or call.data == 'ножницы' and choice == 'бумага':
        for i in range(len(data['results'])):
            if data['results'][i]['user'] == call.from_user.id:
                data['results'][i]['win'] += 1
                break
        await bot.send_message(chat_id=call.from_user.id, text=f'А я выбрала {choice}\nВы победили 🥳')
    with open('database.json', 'w') as f:
        json.dump(data, f)
    await bot.send_message(chat_id=call.from_user.id, text='Выберите один из вариантов', reply_markup=messagemarkup)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)