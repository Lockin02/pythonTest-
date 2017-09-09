# 装饰器

# test1:
def log(func):
	def wrapper(*args, **kw): #wrapper函数可以接受任意参数的调用
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper
@log #相当于执行了语句 now=log(now)
def now():
	print('2015-03-25',[1,3,5])
now()

# test2(decorator需要传入参数):
import functools #导入functools模块

def log2(text):
	def decorator(func):
		@functools.wraps(func)  #原始属性复制到wrapper函数中
		def wrapper(*args, **kw):
			print('%s %s():' % (text,func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator
@log2('execute') #相当于  now=log('execute')(now)
#首先执行log('execute')  返回的是decorator函数 再调用返回的函数，参数是now函数，返回值最终是wrapper函数
def now():
	print('1993-10-23')
now()
print(now.__name__) #输出wrapper
                    
#test3:
import types
import functools

def logfunc(func):
    if isinstance(func, types.FunctionType):
        @functools.wraps(func)
        def wrapper(*arg, **kw):
            print('begin call %s' % func.__name__)
            f = func(*arg, **kw)
            print('end call %s' % func.__name__)
            return f
        return wrapper
    else:
        @functools.wraps(func)
        def decorator(trueFunc):
            def wrapper(*arg, **kw):
                print('begin other call %s(%s)' % (trueFunc.__name__, func))
                f = trueFunc(*arg, **kw)
                print('end other call %s(%s)' % (trueFunc.__name__, func))
                return f
            return wrapper
        return decorator

@logfunc  #相当于 f=logfunc(f())
def f():  
	print('aa')

@logfunc('execute')  #相当于 g=logfunc('execute')(g)
def g():
	print('bb')

print( isinstance(f,types.FunctionType))
print( isinstance('texcute',types.FunctionType))
f()  
g()
