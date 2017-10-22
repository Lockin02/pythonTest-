#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/10/22 16:00
# @Author  : Lockin
# @Site    : 
# @File    : do_wsgi.py.py
# @Software: PyCharm

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]