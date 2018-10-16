# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 0016 下午 9:01
# @Author  : songzxDev
# @Email   : songzx_2326@163.com
# @File    : fortunedrp.py
# @Software: PyCharm
from django.shortcuts import render
from webtreasures.services import fortunedrpservice
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt, csrf_protect


@csrf_exempt
def getincometype(request):
    params = request.GET
    page_info = fortunedrpservice.getincometype(params)
    return JsonResponse(page_info)
