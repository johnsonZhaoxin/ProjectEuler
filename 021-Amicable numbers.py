import math
import numpy as np
from itertools import combinations

def factorize(n):
	result = []	
	for i in range(1,int(np.sqrt(n)+1)):
		if (n%i==0):
			result.append(i)
			result.append(int(n/i))
		result.sort()
	return result

def sumoffactors(n):
	factors = factorize(n)
	sum = 0
	for factor in factors:
		sum +=factor
	return sum-n

#print(factorize(220))
#print(sumoffactors(220))
#print(factorize(284))
#print(sumoffactors(284))

def amicable(a, b):
	if sumoffactors(a) == b and sumoffactors(b) ==a:
		return True
	else:
		return False
comb = combinations(range(2,10001),2)
sum = 0
for item in comb:
	a,b = item
	#print(item)
	if amicable(a,b):
		print(a,b)
		sum+= a+b		
print(sum)
