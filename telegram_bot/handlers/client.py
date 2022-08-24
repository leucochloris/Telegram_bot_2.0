from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove



# @dp.message_handler(commands=['start', 'help'])
async def greeting(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Greeting!\n\nI`m bot-assistant, your guide to the world of English language!\n\n'
                           'About us - /about\nRegistration - /reg\nHelp - /help', reply_markup=kb_client)


# @dp.message_handler(commands=['about'])
async def about_us(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'We are - school of education English language "EASY WAY" 📚📖📕\n\nOur company is young startup with a potential of billion of dollars! 🤑💵💰\n'
                           '\nWe have schools and representative offices in 5 cities. Other 10 cities are in the plans ✈✈✈\n\n')


# @dp.message_handler(commands=['contact'])
async def contact(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Any more questions?\n\nFeel free to contact me: https://vk.com/funnymanalex', reply_markup=ReplyKeyboardRemove())


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(greeting, commands=['start', 'help'])
    dp.register_message_handler(about_us, commands=['about'])
    dp.register_message_handler(contact, commands=['contact'])
