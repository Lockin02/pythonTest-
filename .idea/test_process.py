from multiprocessing import Process
import os

def hello():
    a = 0
    for i in range(10000000):
        a = a + i
        time.sleep(0.000001)
        a = a - i
    print(a)
    print(id(a))

p1 = Process(target=hello)
p2 = Process(target=hello)
p1.start()
p2.start()
p1.join()
p2.join()