from most_frequently_used import *
from itertools import *

# 找出permutation数字
def permute(num):
    num_list = seperate_num(num)
    result = []
    new_permu = permutations(num_list,4)
    for list in new_permu:
        number = generate_num_from_list(list)
        if number not in result:
            result.append(number)
    return result


def possible_combine(per):
    return combinations(per,3)

def validate_arith(Alist):
    # 生成三个元素的列表
    combo = possible_combine(Alist) # 目前是一个tuple
    count = 0

    for numbers in list(combo):
        numbers = list(numbers)
        numbers.sort()
        if numbers[0]+numbers[2]-2*numbers[1] == 0:
            print(numbers)
            count += 1
            break
        else:
            pass
    if count == 0:
        return False
    else:
        return True

#todo 还是有重复的结果。
prime_list = generate_prime_between(1000,10000)
#print(prime_list)

for prime in prime_list:
    per_list = permute(prime)
    per_list.sort()
    #print(per_list)

    filtered = find_same_inAB(per_list,prime_list)
    filtered.sort()

    #验证是不是等差数列
    if len(filtered)>2:
        #print(filtered)
        validate_arith(filtered)

    #最后答案[2969, 6299, 9629]
            



