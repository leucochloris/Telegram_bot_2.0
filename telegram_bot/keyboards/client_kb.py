from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/about')
b2 = KeyboardButton('/programs')
b3 = KeyboardButton('/contact')
# b4 = KeyboardButton('Share your phone number', request_contact=True)  ##### button which send request to user
# b5 = KeyboardButton('Adress request', request_location=True)          ##### button which send request to user


kb_client = ReplyKeyboardMarkup(resize_keyboard=True)#, one_time_keyboard=True)

'''     WHAT KIND OF BUTTONS OUTPUT HAPPENS ?! 
- add - just append button
- insert - insert into free space
- row - just added button in row
'''

kb_client.add(b1).add(b2).add(b3)
# kb_client.row(b1, b2, b3, b4, b5)
# kb_client.add(b1).row(b2, b3).insert(b4)
