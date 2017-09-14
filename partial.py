import functools
int2 = functools.partial(int,base=2)
print(int2('1000000'))

print(int2('1000000',base=10))

# 创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
max2 = functools.partial(max, 10)
#实际上会把10作为*args的一部分自动加到左边，也就是：args = (10, 5, 6, 7) max(*args)
print(max2(3,6,9))