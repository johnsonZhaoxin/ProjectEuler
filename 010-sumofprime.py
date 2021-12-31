import numpy as np
def isprime(n):
    for i in range(2,int(np.sqrt(n)+1)):
        if n%i == 0:
            #print("%d can be divided by %d"%(n,i))
            return False
    #print("%d is a prime number"%n)
    return True

sum = 0
for i in range(2,int(2e6)):
    if isprime(i):
        print(i)
        sum += i
print(sum)