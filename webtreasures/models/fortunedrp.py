# -*- coding: utf-8 -*-
# @Time    : 2018/10/8 0008 下午 9:08
# @Author  : songzxDev
# @Email   : songzx_2326@163.com
# @File    : fortunedrp.py
# @Software: PyCharm

from django.db import models
import django.utils.timezone as timezone


class IncomeType(models.Model):
    type_name = models.CharField(u'收入类型名称', max_length=100, default=u'', unique=True)
    type_code = models.CharField(u'收入类型编码', max_length=100, default=u'', unique=True)
    type_desc = models.CharField(u'收入类型描述', max_length=100, default=u'', null=True)
    add_date = models.DateTimeField(u'数据创建日期', auto_now_add=True)
    mod_date = models.DateTimeField(u'数据更新日期', auto_now=True, null=True)

    class Meta:
        db_table = 'income_type'
        verbose_name = '收入类型'
        verbose_name_plural = '收入类型'
