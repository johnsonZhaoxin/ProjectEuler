from most_frequently_used import seperate_num

def get_binary(num):
    binary_num = bin(num)
    binary_num = binary_num.replace("0b","")
    return binary_num

def is_recursive(list):
    count = 0
    for i in range(len(list)):
        if list[i] == list[-i-1]:
            pass
        else:
            count +=1
            break
    if count == 0:
        return True
    else:
        return False

sum = 0
for i in range(1,1000000):
    num = i
    binary_num = get_binary(i)

    base10list = seperate_num(num)
    base2list = seperate_num(binary_num)
    if is_recursive(base10list) and is_recursive(base2list):
        print(i,binary_num)
        sum += i

print(sum)