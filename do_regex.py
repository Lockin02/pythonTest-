#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/10/14 16:32
# @Author  : Lockin
# @Site    : 
# @File    : do_regex.py
# @Software: PyCharm

import re
e = r'^[a-zA-Z0-9]+.*[a-zA-Z0-9]*\@[a-zA-Z0-9]*.com$'
m1=re.match(e,'someone@gmail.com')
m2=re.match(e,'bill.gates@microsoft.com')
m3=re.match(e,'bill.gates@163.com')
print(m1)
print(m2)
print(m3)