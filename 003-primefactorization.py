import numpy as np
def isprime(n):
    for i in range(2,n-1):
        if n%i == 0:
            print("%d can be divided by %d"%(n,i))
            return False
    print("%d is a prime number"%n)
    return True

def factorize(n):
    res = []
    for i in range(2,int(n/2)):
        if n%i == 0:
            print(i)
            n = n / i
            return factorize(n) #有点问题，如果循环之后没有了没有输出，没有把最后一位数字输出
factorize(600851475143257484)