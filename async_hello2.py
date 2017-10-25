#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/10/25 14:27
# @Author  : Lockin
# @File    : async_hello2.py
# @Software: PyCharm

import threading
import asyncio

async def hello():
    print('Hello world! (%s)' % threading.currentThread())
    await asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()