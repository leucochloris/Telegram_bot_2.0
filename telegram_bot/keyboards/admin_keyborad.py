from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

####### admin keyboard
botton_load = KeyboardButton('/load')
botton_delete = KeyboardButton('/delete')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(botton_load).add(botton_delete)