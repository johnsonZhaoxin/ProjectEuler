from itertools import product
valueofcoin = [1,2,5,10,20,50,100,200]

def sumoflist(coins):
    sum = 0
    for coin in coins:
        sum += coin
    return sum

# 最多是200个，最少是1个，但是采用product由于先后顺序，导致有重复。会比较麻烦。
ways = 0
possible = []
# 先试试9个硬币
for i in range(1,10):
    coins_list = list(product(valueofcoin,repeat=i))
    for coins in coins_list:
        if sumoflist(coins) == 200:
            ways += 1
            print(coins)
            possible.append(coins)
print(ways)

