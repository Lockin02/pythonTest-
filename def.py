def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

def cale_list(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

def cale_num(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

def person_onekey(name,sex,**kw):
    print('name:',name,'sex:',sex,'other:',kw)

def person_definekey(name,age,*,city="珠海",identifient):
    print(name,age,city,identifient)

print(add_end([1,2]))

print(cale_list([1,2,3]))

print(cale_num(1,2,3))

num_list = [1,2,3]
print(cale_num(*num_list))

person_onekey('Lockin','男',city="珠海",identifient="程序员")

extra_onekey = {'city':'珠海', 'identifient':"程序员"}
person_onekey('Lockin','男',city=extra_onekey['city'],identifient=extra_onekey['identifient'])

extra_somekey = {'city': 'Beijing', 'job': 'Engineer'}
person_onekey('Lockin','男',**extra_somekey)

person_definekey('Lockin','15',identifient='程序员')