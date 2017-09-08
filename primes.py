def _odd_iter():
    n = 1
    while True:
        n = n+2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)

# 打印1000以内的素数:
for n in primes():
    # print('判断外面：', (n))
    if n < 2:
        # print('判断里面：',(n))
        pass
    else:
        break