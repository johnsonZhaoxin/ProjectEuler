from itertools import combinations

# 公式写出来了，但是跑起来太费时间了，需要优化
def validate(list):
    for i in range(1,len(list)-1):
        if abs(list[i]**2-list[i-1]*list[i+1])>2:
            return False
    return True

def generate_possible(list):
    result = []
    for i in range(5,len(list)+1):
        result.append(combinations(list,i))

    seq_list = []
    for possible_item in result:
        for actual in possible_item:
            seq_list.append(actual)
    return seq_list

def G(n):
    count = 0
    origin_list = list(range(1,n+1))
    seq_list = generate_possible(origin_list)
    for seq in seq_list:
        if validate(seq):
            count += 1
        else:
            continue
    return count

print(G(10))