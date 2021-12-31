import math

def multiples(n):
    result = []
    for i in range(1,n,1):
        if i%3==0 or i%5==0:
            print(i)
            result.append(i)
    return result

multiples_result =multiples(1000)
sum = 0
for i in multiples_result:
    sum +=i

print(sum)