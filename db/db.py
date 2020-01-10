from django.db import connection

def select_bioday(user_code):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM biomatric_day where user_id = {}".format(user_code))
    a = cursor.fetchall()
    return a[0]

def select_bio_RT(user_code, date):
    cursor = connection.cursor()
    sql = "SELECT RT_HR, RT_RR, RT_SV, RT_HRV FROM biomatric_rt WHERE user_id = {} and DATE(rt_create_time) between '2019-11-11' and '2019-11-12';".format(user_code)
    cursor.execute(sql)
    a = cursor.fetchall()
    return a

def latest_select():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM biomatric_rt ORDER BY RT_CREATE_TIME DESC limit 1")
    a = cursor.fetchall()
    return a

def select_myinfo(user_code):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM myinfo where user_id = {}".format(user_code))
    a = cursor.fetchall()
    return a[0]

def find_start_end_sleep(user_code, date):
    cursor = connection.cursor()
    sql = "select SLEEP_START_TIME, SLEEP_END_TIME from C_SLEEP_ANALYSIS where \
        USER_CODE = {} AND SA_CREATE_DATE = {}".format(user_code, date)
    cursor.execute(sql)
    a = cursor.fetchall()
    return a