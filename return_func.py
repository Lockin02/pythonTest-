#函数作为返回值

# test1:
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1,3,5,7)
print(f())

# 每次调用返回一个新的函数 调用结果互不影响
f2 = lazy_sum(1, 3, 5, 7, 9)
f1 = lazy_sum(1, 3, 5, 7, 9)
print(f1==f2)

# test2(返回函数不是立即执行 直到调用才执行)：
def count():
    fs = []
    for i in range(1,4):
        def f():
            return  i * i
        fs.append(f)
    return fs
f3,f4,f5 = count()
print(f3())
print(f4())
print(f5())

# test3
# 返回函数不要引用任何循环变量，或者后续会发生变化的变量 若要引用 再创建一个函数
def def_count():
    def f(j):
        def g():
            return j*j
        return  g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs

f6,f7,f8 = def_count()
print(f6())
print(f7())
print(f8())
