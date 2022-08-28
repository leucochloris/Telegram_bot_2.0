from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db



# @dp.message_handler(commands=['start', 'help'])
async def greeting(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Greeting!\n\nI`m bot-assistant, your guide to the world of English language!\n\n'
                           'About us - /about\nOur programs - /programs\nRegistration - /reg\nContact us - /contact', reply_markup=kb_client)


# @dp.message_handler(commands=['about'])
async def about_us(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'We are - school of education English language "EASY WAY" 📚📖📕\n\nOur company is young startup with a potential of billion of dollars! 🤑💵💰\n'
                           '\nWe have schools and representative offices in 5 cities. Other 10 cities are in the plans ✈✈✈\n\n')


# @dp.message_handler(commands=['contact'])
async def contact(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Any more questions?\n\nFeel free to contact me: https://vk.com/funnymanalex')#, reply_markup=ReplyKeyboardRemove()) ------ hide keyborad


@dp.message_handler(commands=['programs'])
async def learning_programs(message : types.Message):
    await sqlite_db.sql_read(message)




# #### feature for SMART BOT
#
# @dp.message_handler(lambda message: 'taxi' in message.text)
# async def taxi(message: types.Message):
#     await message.reply('Try to check: https://call-taxi.ru/')


###### declaration of our handlers
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(greeting, commands=['start', 'help'])
    dp.register_message_handler(about_us, commands=['about'])
    dp.register_message_handler(contact, commands=['contact'])
    dp.register_message_handler(learning_programs, commands=['programs'])
