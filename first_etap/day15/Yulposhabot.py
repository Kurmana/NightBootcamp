
import logging
#import requests
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6065351917:AAGd-NpZerKU4rN-iR9teR6RBGLlvVZW6ls'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher !!! ОТВЕЧАЕТ ЗА ВСЕ СООБЩЕНИЯ КОТОРЫЕ приходят к боту, БОТ ОТВЕЧАЕТ
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
# это декоратор, отвечает за то какие сообщения будут поступать боту

@dp.message_handler(commands=['start', 'help'])
# данная асинхронная функция начинает срабатывать, когда запишут старт или хелп, отвечает какие будут функции отвечать
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm Yulposha!")
    #это сообщение будет получать человек при вводе команды

# все остальные запросы которые будут поступать будет обрабатывать функиция ECHO, в аргументах мессеж
@dp.message_handler()
async def echo(message: types.Message):
    # print(message)  ## мы можем так увидеть полную инф по сообщениям, которую отправили нашему боту
    # requests.post('https://api.telegram.org/bot6065351917:AAGd-NpZerKU4rN-iR9teR6RBGLlvVZW6ls/sendMessage')
    if message.text == "Aichurek":
        await message.answer("hello Aichurek, welcome")
    elif message.text == "Aijan":
        await message.answer("hello Aijan, welcome")
    else:
        await message.answer('I dont know you, who are you?')

# это учловие нужно чтобы запустить файл
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)