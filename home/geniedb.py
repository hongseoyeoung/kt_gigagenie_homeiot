from django.db import connection
from .make_vo import makeVo
def insert():
    cursor = connection.cursor()
    cursor.execute("INSERT INTO genie(id, name) VALUES({},'{}')".format(1, 'kim'))
    cursor.fetchall()

def select():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM genie")
    a = cursor.fetchall()
    for i in a:
        print(i)

def show_table():
    cursor = connection.cursor()
    cursor.execute("show full columns from genie;")
    a = cursor.fetchall()
    makeVo("user1", a)
    