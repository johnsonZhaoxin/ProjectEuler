from most_frequently_used import *

def reduced_list_from_left(num):
    result = []
    length = len(str(num))
    for i in range(1,length):
        orgin_list = seperate_num(num)
        for j in range(0,i):
            orgin_list.pop(0) #一定要pop(0), 因为删除之后下面的元素就是第一个了
        reduced_num = generate_num_from_list(orgin_list)
        result.append(reduced_num)
    return result

def reduced_list_from_right(num):
    result = []
    length = len(str(num))
    for i in range(1, length):
        orgin_list = seperate_num(num)
        for j in range(0, i):
            orgin_list.pop(-1)
        reduced_num = generate_num_from_list(orgin_list)
        result.append(reduced_num)
    return result

prime_list = generate_prime_under(999999)

count = 0
i = 7 #从23开始 因为2,3,5,7,11,13,17都不算的应该
while count <= 11:
    prime_num = prime_list[i]
    left_list = reduced_list_from_left(prime_num)
    right_list = reduced_list_from_right(prime_num)
    all_list = left_list + right_list
    criterion = 0

    for reduced_num in all_list:
        if isprime(reduced_num):
            pass
        else:
            criterion += 1
            break
    if criterion == 0:
        print(prime_num)
        count += 1
    i += 1