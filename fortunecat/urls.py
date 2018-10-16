# -*- coding: utf-8 -*-
"""fortunecat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from webtreasures.views import fortunedrp

"""
url()函数可以传递4个参数，其中2个是必须的：regex和view，以及2个可选的参数：kwargs和name。下面是具体的解释：

regex：
regex是正则表达式的通用缩写，它是一种匹配字符串或url地址的语法。Django拿着用户请求的url地址，在urls.py文件中对urlpatterns列表中的每一项条目从头开始进行逐一对比，一旦遇到匹配项，立即执行该条目映射的视图函数或二级路由，其后的条目将不再继续匹配。因此，url路由的编写顺序至关重要！
需要注意的是，regex不会去匹配GET或POST参数或域名，例如对于https://www.example.com/myapp/，regex只尝试匹配myapp/。对于https://www.example.com/myapp/?page=3,regex也只尝试匹配myapp/。

如果你想深入研究正则表达式，可以读一些相关的书籍或专论，但是在Django的实践中，你不需要多高深的正则表达式知识。

性能注释：正则表达式会进行预先编译当URLconf模块加载的时候，因此它的匹配搜索速度非常快，你通常感觉不到。

view：
当正则表达式匹配到某个条目时，自动将封装的HttpRequest对象作为第一个参数，正则表达式“捕获”到的值作为第二个参数，传递给该条目指定的视图。如果是简单捕获，那么捕获值将作为一个位置参数进行传递，如果是命名捕获，那么将作为关键字参数进行传递。

kwargs：
任意数量的关键字参数可以作为一个字典传递给目标视图。

name：
对你的URL进行命名，可以让你能够在Django的任意处，尤其是模板内显式地引用它。相当于给URL取了个全局变量名，你只需要修改这个全局变量的值，在整个Django中引用它的地方也将同样获得改变。这是极为古老、朴素和有用的设计思想，而且这种思想无处不在。
"""

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^getincometype/$', fortunedrp.getincometype, name='getincometype')
]
