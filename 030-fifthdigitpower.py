import math
def judgedigitpower(n):
    num = str(n)
    sum = 0
    for item in num:
        #print(item)
        sum += int(item)**5
    if sum == n:
        return True
    else:
        return False
#todo 为什么超过7位数就不能满足要求了。
#解释最大是9^5,7位数的最大值就是413343,所以六位数就到头了

for i in range(1,int(1e10)):
    if judgedigitpower(i):
        print(i)
