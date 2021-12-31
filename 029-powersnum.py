from itertools import product
viableab = list(product(range(2,101),repeat=2))
result = []
for item in viableab:
    a,b = item
    #print(a,b)
    power = a**b
    if power not in result:
        result.append(power)
result.sort()
print(len(result))