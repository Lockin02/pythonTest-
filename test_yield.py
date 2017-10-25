#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/10/25 11:46
# @Author  : Lockin
# @File    : test_yield.py
# @Software: PyCharm

def countdown(n):
    print("Counting down from", n)
    while n >= 0:
        newvalue = (yield n)
        # If a new value got sent in, reset n with it
        if newvalue is not None:
            n = newvalue
        else:
            n -= 1


c = countdown(10)
for x in c:
    print(x)
    if x == 10:
        c.send(3)
