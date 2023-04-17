import logging
#import requests
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6065351917:AAGd-NpZerKU4rN-iR9teR6RBGLlvVZW6ls'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    #requests.post('https://api.telegram.org/bot6065351917:AAGd-NpZerKU4rN-iR9teR6RBGLlvVZW6ls/sendMessage', {'chat_id': 5613130710, 'text': f'Пришло сообщение из бота {message}'})
    if message.text == 'Artem':
        await message.answer('Здравствуйте Артем, рад вас приветствовать')
    elif message.text == 'Ernest':
        await message.answer('Йоу как тты чувак')
    else:
        await message.answer('Я тебя не знаю, ты кто?')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)