import math
import numpy as np
from itertools import combinations

def factorize(n):
	result = []
	for i in range(1,int(np.sqrt(n)+1)):
		if (n%i==0):
			result.append(i)
			#只保留一半数字就好了
			#result.append(int(n/i))
		result.sort()
	#result.remove(n)
	return result

def get_multipy_num(n,factor):
	quotient = int(n/factor)
	num = []
	#print("%d * %d = %d"%(factor,quotient,n))
	expressionstr = str(factor)+str(quotient)+str(n)
	for digit in expressionstr:
		num.append(int(digit))
	num.sort()
	return num

def judge_pandigitial(num):
	if num == list(range(1,10)):
		return True
	else:
		return False

#todo 证明最多是4位数才能把1-9九个数字全部用起来
for i in range(999,10000):
	factors_list =factorize(i)
	#print(factors_list)
	for factor in factors_list:
		num = get_multipy_num(i,factor)
		#print(num)
		if judge_pandigitial(num):
			print(i)
			break
		else:
			pass
