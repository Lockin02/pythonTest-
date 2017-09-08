from  math import  sqrt

def do_sth(l,ash):
    return [ash(x_k) for x_k in l]

def ash(x):
    return  hex(int(sqrt(abs(x))))

print(do_sth([1,-4,16,25],ash))