from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db


class Cust_Reg(StatesGroup):
    name = State()
    surname = State()
    age = State()
    city = State()
    level = State()
    phone = State()


# bigin talking of registration (START OF THE STATUS MACHINE)
# @dp.message_handler(commands='reg', state=None)
async def reg_start(message: types.Message):
    await Cust_Reg.name.set()
    await message.reply('Specify your name ')



###### canсel handler
# @dp.message_handler(state='*', commands=['cancel'])
# @dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('OK!')


# catch #1 answered from users
# @dp.message_handler(state=Cust_Reg.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await Cust_Reg.next()
    await message.reply('Now specify your surname ')


# catch #2 answered from users
# @dp.message_handler(state=Cust_Reg.surname)
async def load_surname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['surname'] = message.text
    await Cust_Reg.next()
    await message.reply('Now specify your age ')


# catch #3 answered from users
# @dp.message_handler(state=Cust_Reg.age)
async def load_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text
    await Cust_Reg.next()
    await message.reply('Now specify your city ')


# catch #4 answered from users
# @dp.message_handler(state=Cust_Reg.city)
async def load_city(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text
    await Cust_Reg.next()
    await message.reply('Now specify your level of knowledge ------> A1,2 | B1,2 | C1,2')


# catch #5 answered from users
# @dp.message_handler(state=Cust_Reg.level)
async def load_level(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['level'] = message.text
    await Cust_Reg.next()
    await message.reply('Now specify your phone number ')


# catch #6 answered from users
# @dp.message_handler(state=Cust_Reg.phone)
async def load_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
    await sqlite_db.sql_add_registration(state)
    await state.finish()




###### declaration of our handlers
def register_handlers_registration(dp: Dispatcher):
    dp.register_message_handler(reg_start, commands=['reg'], state=None)
    dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(load_name, state=Cust_Reg.name)
    dp.register_message_handler(load_surname, state=Cust_Reg.surname)
    dp.register_message_handler(load_age, state=Cust_Reg.age)
    dp.register_message_handler(load_city, state=Cust_Reg.city)
    dp.register_message_handler(load_level, state=Cust_Reg.level)
    dp.register_message_handler(load_phone, state=Cust_Reg.phone)





