#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Lockin Lee'

import sys

def test():
	# sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()


# 第三方库测试
from PIL import Image
im = Image.open('D:\python\pythonTest-\\testpic.jpg')
print(im.format,im.size,im.mode)
