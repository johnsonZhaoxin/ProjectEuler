from most_frequently_used import *
from itertools import combinations
from constants import *

prime_list = prime_list_under_one_million
possible_seq = combinations(range(len(prime_list)),2)

def sumisprime(m,n):
    sum = sum_of_list(prime_list,m,n)
    if sum <int(1e6) and isprime(sum):
        return True
    else:
        return False


def sum_of_list(list,m,n):
    sum = 0
    for i in range(m,n):
        sum+= list[i]
    return sum

# 主程序
count = 0
max_consecutive = 0
max_m=0
max_n=0
max_prime=0
for seq in possible_seq:
    m,n =seq
    if sumisprime(m,n):
        #print("start from %d prime to %d prime. "%(m+1,n),end="total ")
        #print(n-m,end=" primes, and the sum is ")
        #print(sum_of_list(prime_list, m, n))
        count += 1
        if n-m > max_consecutive:
            max_consecutive = n-m
            max_m = m
            max_n = n
            max_prime = sum_of_list(prime_list, m, n)
        else:
            pass
print(count)
print(max_m,max_n,max_prime)

#48798个满足要求的数字
#3 546 997651