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





async def new_users(message):
    for new_st in cur.execute('SELECT * FROM students where is_active = 0').fetchall():
        # await bot.send_message(message.from_user.id,  f'{new_st[1]}\n\nDescription: {new_st[2]}\n\nPrice: {new_st[6]}')
        await message.reply(f'New *lead #{new_st[0]}*, need to call!\n\nName: *{new_st[1]} {new_st[2]}*\nNumber: *{new_st[6]}*\nCity: *{new_st[3]}*\nJoin to us at *{new_st[7]}*', parse_mode= "Markdown")






def registration():
    global base, cur
    base = sq.connect('school_easy_way.db')
    cur = base.cursor()
    base.execute('CREATE TABLE IF NOT EXISTS students (name TEXT, surname TEXT, age TEXT, city TEXT, level TEXT, phone INTEGER)')
    base.commit()



async def sql_add_registration(state):
    async with state.proxy() as data2:
        cur.execute("INSERT INTO students (name, surname, age, city, level, phone) VALUES (?, ?, ?, ?, ?, ?)", tuple(data2.values()))
        base.commit()