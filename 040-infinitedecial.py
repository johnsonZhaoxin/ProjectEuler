from most_frequently_used import generate_num_from_list
from functools import lru_cache

@lru_cache(maxsize=None)
def generate_decimal(n):
    num_list = list(range(1,n+1))
    num = generate_num_from_list(num_list)
    return num

def get_nth_digit(num,nth):
    if len(str(num)) < nth:
        print("小数点后位数不足")
        return None
    else:
        return str(num)[nth-1]

num = generate_decimal(200000)
#print(len(str(num)))
#todo 要多少位才可以有小数点后1,000,000位,目前发现是200000个

#主程序
product = 1
for i in range(7):
    digit = get_nth_digit(num,10**i) #搜寻的速度太慢了。布置什么原因
    print(digit)
    product *= int(digit)

print(product)

#答案 1
#1
#5
#3
#7
#2
#1
#210