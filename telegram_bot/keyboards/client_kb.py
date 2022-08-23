from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/start')
b2 = KeyboardButton('/about')
b3 = KeyboardButton('/contact')

kb_client = ReplyKeyboardMarkup()

kb_client.add(b1).add(b2).add(b3)