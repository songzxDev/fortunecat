# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 0016 下午 9:07
# @Author  : songzxDev
# @Email   : songzx_2326@163.com
# @File    : fortunedrpservice.py
# @Software: PyCharm
from webtreasures.dbs import fortunedrpdb


def getincometype(params):
    _result = fortunedrpdb.select_incometype()

    return {'returncode': 0, 'msg': '', 'result': _result}
