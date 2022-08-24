import sqlite3 as sq

def sql_start():
    global base, cur
    base = sq.connect('school_easy_way.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.execute('CREATE TABLE IF NOT EXISTS programs (img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO programs VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()