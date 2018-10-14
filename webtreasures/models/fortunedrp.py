# -*- coding: utf-8 -*-
# @Time    : 2018/10/8 0008 下午 9:08
# @Author  : songzxDev
# @Email   : songzx_2326@163.com
# @File    : fortunedrp.py
# @Software: PyCharm

from django.db import models
import django.utils.timezone as timezone


# 收入类型
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


# 收入明细
class IncomeDetail(models.Model):
    goods_code = models.CharField(verbose_name=u'商品编码', max_length=100, default='', null=False, db_column='goods_code')
    money_amount = models.FloatField(verbose_name=u'收入金额', default=0.00, null=False, db_column='money_amount')
    type_code = models.CharField(verbose_name=u'收入类型', null=False, max_length=100, db_column='type_code')
    income_date = models.DateTimeField(verbose_name=u'入账日期', null=False, default=timezone.now, db_column='income_date')
    add_date = models.DateTimeField(verbose_name=u'数据创建日期', auto_now_add=True)
    mod_date = models.DateTimeField(verbose_name=u'数据更新日期', auto_now=True, null=True)
    logic_del = models.IntegerField(verbose_name=u'逻辑删除', default=0, null=False, db_column='logic_del')

    class Meta:
        db_table = 'income_detail'
        verbose_name = '收入明细'
        verbose_name_plural = '收入明细'
