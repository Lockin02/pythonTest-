#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/10/22 16:20
# @Author  : Lockin
# @Site    : 
# @File    : do_wsgi_server.py.py
# @Software: PyCharm

# 从wsgiref模块导入:
from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数:
from do_wsgi import application

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 9999, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()