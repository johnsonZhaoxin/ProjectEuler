from most_frequently_used import *

# 删除元素
def Delete_from_num(origin_list,num):
    pop_list = seperate_num(num)
    for element in pop_list:
        origin_list.remove(element)
    return origin_list

# 答案为932718654
number_list = list(range(1,10))