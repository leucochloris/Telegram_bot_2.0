from aiogram import types, Dispatcher
from create_bot import dp


# @dp.message_handler()
async def echo_send(message: types.Message):
    # await message.answer(message.text)                         #################### отправить сообщение
    await message.reply('Oops, something wrong....')  ###################### ответить на сообщение
    # await bot.send_message(message.from_user.id, message.text) ######################## написать в ЛС


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)