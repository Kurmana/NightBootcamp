import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6065351917:AAGd-NpZerKU4rN-iR9teR6RBGLlvVZW6ls'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\n this is exchange\n welcome")

@dp.message_handler()
async def echo(message: types.Message):
    if len(message.text.split(' ')) == 2:
        if message.text.split(' ')[1].lower == 'rubbles':
            await message.answer(f'in som it is {int(message.text.split(" ")[0])* 1.06}')
        elif message.text.split(' ')[1].lower == 'dollars':
            await message.answer(f'in som it is {int(message.text.split(" ")[0])* 87.42}')
        elif message.text.split(' ')[1].lower == 'tenge':
            await message.answer(f'in som it is {int(message.text.split(" ")[0])* 0.19}')
        else:
            await message.answer('please enter dollars, rubbles, tenge')
    else:
        await message.answer('wrong typing')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)