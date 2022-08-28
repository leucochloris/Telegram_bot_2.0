import sqlite3 as sq
from create_bot import dp, bot
from aiogram.dispatcher.filters.state import State, StatesGroup


def sql_start():
    global base, cur
    base = sq.connect('school_easy_way.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!\nRegistration is allow.')
    base.execute('CREATE TABLE IF NOT EXISTS programs (img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO programs VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_read(message):
    for i in cur.execute('SELECT * FROM programs').fetchall():
        await bot.send_photo(message.from_user.id, i[0], f'{i[1]}\n\nDescription: {i[2]}\n\nPrice: {i[-1]}')







def registration():
    global base, cur
    base = sq.connect('school_easy_way.db')
    cur = base.cursor()
    base.execute('CREATE TABLE IF NOT EXISTS students (name TEXT, surname TEXT, age TEXT, city TEXT, level TEXT, phone INTEGER)')
    base.commit()



async def sql_add_registration(state):
    async with state.proxy() as data2:
        cur.execute('INSERT INTO students VALUES (?, ?, ?, ?, ?, ?)', tuple(data2.values()))
        base.commit()