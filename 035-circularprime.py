from collections import deque
from functools import lru_cache

from most_frequently_used import isprime, seperate_num


@lru_cache(maxsize=None)
def generate_prime_under(size):
    result = []
    for i in range(2,size+1):
        if isprime(i):
            result.append(i)
    return result

def generate_num_from_list(list):
    num = ''
    for i in list:
        #print(str(i))
        num += str(i)
    return int(num)

def create_cicurlar(list):
    result = []
    for i in range(1,len(list)):
        queue = deque(list)
        queue.rotate(-i)
        result.append(queue)
    return result

# 主程序
prime_list = generate_prime_under(1000000)
#print(prime_list)


count = 0
for prime in prime_list:
    #切分数字
    num_list = seperate_num(prime)

    #利用create_circular创造按列表循环数字
    new_list = create_cicurlar(num_list)

    i = 0
    for new_num in new_list:
        newNum = generate_num_from_list(new_num)
        if not isprime(newNum): #也可以用not in prime_list，但是极费时间。搜寻列表不如单独判断
            i += 1
            break
        else:
            pass

    if i == 0:
        print(prime)
        count += 1
print(count)


