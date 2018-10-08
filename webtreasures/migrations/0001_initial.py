# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-10-08 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IncomeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(default='', max_length=100, unique=True, verbose_name='\u6536\u5165\u7c7b\u578b\u540d\u79f0')),
                ('type_code', models.CharField(default='', max_length=100, unique=True, verbose_name='\u6536\u5165\u7c7b\u578b\u7f16\u7801')),
                ('type_desc', models.CharField(default='', max_length=100, verbose_name='\u6536\u5165\u7c7b\u578b\u63cf\u8ff0')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='\u6570\u636e\u521b\u5efa\u65e5\u671f')),
                ('mod_date', models.DateTimeField(auto_now=True, verbose_name='\u6570\u636e\u66f4\u65b0\u65e5\u671f')),
            ],
        ),
    ]