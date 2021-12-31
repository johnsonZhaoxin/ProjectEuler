import numpy as np
from itertools import product

#最后结果-61, 971

#这里由于考虑到多项式的结果为负数，需要排除
def isprime(n):
    if n < 2:
        return False
    else:
        for i in range(2,int(np.sqrt(n)+1)):
            if n%i == 0:
                #print("%d can be divided by %d"%(n,i))
                return False
        #print("%d is a prime number"%n)
        return True

def polynomial(a,b,x):
    return x**2+a*x+b


num = 0
for item in product(range(0,10),repeat=2):
    i = 0
    a,b = item
    while isprime(polynomial(a,b,i)):#while循环有点问题，可能第一个就不是prime number
        i += 1
    print(a,b,i)


