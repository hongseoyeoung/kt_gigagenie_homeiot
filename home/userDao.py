from django.db import connection

def insert():
    cursor = connection.cursor()
    cursor.execute("INSERT INTO DLC_USER(id, name) VALUES({},'{}')".format(1, 'kim'))
    cursor.fetchall()

def select():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM DLC_SENSORDATA")
    a = cursor.fetchall()
    return a

def latest_select():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM DLC_SENSORDATA ORDER BY USD_CREATED_DATE DESC limit 1")
    a = cursor.fetchall()
    return a

def show_table():
    cursor = connection.cursor()
    cursor.execute("show full columns from genie;")
    a = cursor.fetchall()
