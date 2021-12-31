def isprime(n):
    for i in range(2,n-1):
        if n%i == 0:
            #print("%d can be divided by %d"%(n,i))
            return False
    #print("%d is a prime number"%n)
    return True

n = 1
num = 2
while n <=10001:
    if isprime(num):
        print("第%d个质数是%d"%(n,num))
        n +=1
        num +=1
    else:
        num +=1
