from django.db import connection

def select_bioday(user_id):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM biomatric_day where user_id = {}".format(user_id))
    a = cursor.fetchall()
    return a[0]

def select_bio_RT(user_id, date):
    cursor = connection.cursor()
    sql = "SELECT RT_HR, RT_HRV FROM biomatric_rt WHERE user_id = {} and DATE(rt_create_time) between '2019-11-11' and '2019-11-12';".format(user_id)
    cursor.execute(sql)
    a = cursor.fetchall()
    return a

