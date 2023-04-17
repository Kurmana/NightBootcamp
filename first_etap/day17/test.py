import logging
from aiogram import Bot, Dispatcher, executor, types
import random
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup

markup = ReplyKeyboardMarkup(resize_keyboard=True)
markup.add(KeyboardButton('/start'), KeyboardButton('/help'), KeyboardButton('/adv'))

API_TOKEN = '5905419861:AAFh-b-Kr15zVvvg16AcaJmm8Cye7HnQ5Uw'


LIST_COMMANDS = '''
<b>/intel</b>📚 - <em>список задач связанных с интеллектуальной работой</em>
<b>/physic</b>💪🏻 - <em>список задач связанных с физической работой</em>
<b>/fun</b>🥳 - <em>задачи для веселья</em>
'''

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Бот успешно запущен')

intel = {
    "читай": "прочитай одну статью в интернете",
    "стихотворение": "выучи одно стихотворение",
    "шахматы": "поиграй шахматы с ботом",
    "codewars": "реши три задачи в codewars",
    "English": "выучи десять новых слов на английском языке"
}

physic = {
    "приседание": "сделай 40 приседаний",
    "йога": "поделй йогу 40 минут",
    "пробежка": "пробежка 30 минут",
    "пресс": "покачай пресс в течение 5 минут",
    "дыши":"закрой глаза и подыши медленно и осознанно в течение 5 минут"
}

fun = {
    "кино": "посмотри свой любимый фильм",
    "музыка": "послушай свою любимую музыку",
    "звонок другу": "позвони лучшему другу",
    "Youtube":"посмотри любимые видео на ютубе",
    "еда": "разреши себе съесть вредную, но любимую еду"
}

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(text=f'Начинаем игру{LIST_COMMANDS}', reply_markup=markup, parse_mode='HTML')

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text='"Привет, друг!\nЯ помогу тебе выбрать случайные задания\nТы согласен? Тогда нажми /start.")', reply_markup=markup)

@dp.message_handler(commands=['adv'])
async def adv_command(message: types.Message):
    await message.answer('Команда девчонок вперед! 👊', reply_markup=markup)
    await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEIm05kO_VM7kobIm2lnv91GSyyZVxI3wACkRIAAvzw4UodOfjG8l2Msy8E')

@dp.message_handler(commands=['intel'])
async def help_command(message: types.Message):
    await message.answer(random.choice(list(intel.values())))

@dp.message_handler(commands=['physic'])
async def help_command(message: types.Message):
    await message.reply(random.choice(list(physic.values())))

@dp.message_handler(commands=['fun'])
async def help_command(message: types.Message):
    await message.reply(random.choice(list(fun.values())))


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)



