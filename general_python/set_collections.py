import sqlite3
import pandas as pd
from pandasql import sqldf
from pandasql import load_births


# print(sqlite3.version)
# print(sqlite3.sqlite_version)

def memory_sql_database():
    db = sqlite3.connect(':memory:')
    # to connect an existing DB, in our case we connect to out memory and not remote DB
    cursor = db.cursor()
    # Use to iterate over the DB
    cursor.execute('''CREATE TABLE books(id INTEGER PRIMARY KEY,title TEXT, author TEXT, price TEXT, year TEXT)''')
    db.commit()
    cursor.execute('''INSERT INTO books values(1,'pro powerShell','Bryan', 35.00, 2015)''')
    cursor.execute('''INSERT INTO books values(2,'Hothiker','Adams', 12.00, 199)''')
    db.commit()
    lsbooks = cursor.execute('''select * from books;''').fetchall()
    dfbook = pd.read_sql_query("SELECT * FROM books", db)
    db.commit()
    print(lsbooks)
    print(dfbook.head())
    cursor.close()


def chinook_sql_database():
    conn = sqlite3.connect('chinook.db')
    # to connect an existing DB, in our case we connect to out memory and not remote DB
    cursor = conn.cursor()
    # Use to iterate over the DB
    albums = cursor.execute('''select * from albums order by title limit 3;''').fetchall()
    # fetchall read all records into memory and return a list.
    print(albums)

    dfalbum = pd.read_sql_query("SELECT * FROM albums", conn)
    print(dfalbum.head())
    dftablist = pd.read_sql_query("SELECT name FROM sqlite_master where type = 'table';", conn)
    print(dftablist.head())
    conn.close()
    i = 4


if __name__ == '__main__':
    chinook_sql_database()
    # memory_sql_database()
