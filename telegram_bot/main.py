from aiogram.utils import executor
from create_bot import  dp
from handlers import client, other, admin
from data_base import sqlite_db

async def on_startup(_):
    print('Bot begin her work....')
    sqlite_db.sql_start()


##### here we leave our regist of handlers

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
