import math
def selfpower(x):
    return pow(x,x)
sum = 0
for i in range(1,1001):
    sum += selfpower(i) #为什么这样的数值类运算就很快
print(sum)