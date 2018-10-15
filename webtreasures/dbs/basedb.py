# -*- coding: utf-8 -*-
# @Time    : 2018/10/15 0015 下午 9:17
# @Author  : songzxDev
# @Email   : songzx_2326@163.com
# @File    : basedb.py
# @Software: PyCharm


from django.db import connection, transaction


# 执行django原始sql语句  并返回一个数组对象
def execute_query(sql):
    cursor = connection.cursor()  # 获得一个游标(cursor)对象
    cursor.execute(sql)
    raw_data = cursor.fetchall()
    col_names = [desc[0] for desc in cursor.description]

    result = []
    for row in raw_data:
        obj_dict = {}
        # 把每一行的数据遍历出来放到dict中
        for index, value in enumerate(row):
            print index, col_names[index], value
            obj_dict[col_names[index]] = value

        result.append(obj_dict)
    cursor.close()
    return result
