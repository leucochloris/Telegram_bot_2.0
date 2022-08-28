from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from keyboards import admin_keyborad

ID = None


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


###### gits ID of current administration
# @dp.message_handler(commands=['moderator', is_chat_admin=True])
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'I hear you....', reply_markup=admin_keyborad.button_case_admin)
    await message.delete()


###### begin conversation of load function (price list)
# @dp.message_handler(commands='load', state=None)
async def cm_start(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.photo.set()
        await message.reply('Load a photo')


###### canсel handler
# @dp.message_handler(state='*', commands=['cancel'])
# @dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('OK!')


###### catching first answer and create a dictionary
# @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
            await FSMAdmin.next()
            await message.reply('Now append how it call')


###### catching second answer
# @dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
            await FSMAdmin.next()
            await message.reply('Now append description of ot')


###### catching third answer
# @dp.message_handler(state=FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
            await FSMAdmin.next()
            await message.reply('Now specify a coast of it')


###### catching final answer
# @dp.message_handler(state=FSMAdmin.price)
async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = message.text
            await message.reply('New element of programs added to database')
        await sqlite_db.sql_add_command(state)
        await state.finish()


###### declaration of our handlers
def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['load'], state=None)
    dp.register_message_handler(cancel_handler, state='*', commands='cancel')
    dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)
