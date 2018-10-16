# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 0016 下午 9:10
# @Author  : songzxDev
# @Email   : songzx_2326@163.com
# @File    : fortunedrpdb.py
# @Software: PyCharm
from webtreasures.dbs import basedb

def select_incometype():
    _sql = 'select id as type_id,type_code,type_name from income_type'
    return basedb.execute_query(_sql)
