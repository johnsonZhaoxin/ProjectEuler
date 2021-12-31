from functools import lru_cache
@lru_cache(maxsize=None)
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)

def seperate_num(num):
    digits = []
    [digits.append(int(i)) for i in str(num)]
    return digits

def get_digit_factorial(num):
    digits = seperate_num(num)
    sum = 0
    for i in digits:
        sum += factorial(i)
    return sum

# 主程序
# todo 需要明确到多少位就不可能了 仅有145 40585这两个数字
for i in range(3,int(1e5)):
    digit_factorial_sum = get_digit_factorial(i)
    if digit_factorial_sum == i:
        print(i)