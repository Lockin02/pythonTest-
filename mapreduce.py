# -*- coding: utf-8 -*-
from functools import reduce

# 测试1题目：
def normalize(name):
    return name.capitalize()

# 测试2题目：
def prod(L):
    return reduce(lambda x,y:x*y ,L)

# 测试1题目：
def str2float(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    return reduce(fn, map(char2num, s.split('.')[0])) + reduce(fn, map(char2num, s.split('.')[1])) / 10 ** len(
        s.split('.')[1])


# 测试1：
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# 测试2：
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

# 测试3：
print('str2float(\'123.456\') =', str2float('123.456'))


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

# **运算符测试
s = '156';
print(reduce(lambda x,y:x*10+y ,map(char2num,s))/10 ** len(s))