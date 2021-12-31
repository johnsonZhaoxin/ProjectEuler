import numpy as np

def factorize(n):
	result = []	
	for i in range(1,int(np.sqrt(n)+1)):
		if (n%i==0):
			result.append(i)
			result.append(int(n/i))
	result.sort()
	result.remove(n)
	#还需要删除完全平方数的分子
	if np.sqrt(n) - int(np.sqrt(n)) <1e-7:
		result.remove(int(np.sqrt(n)))
	return result

def isAbundant(n):
	factors = factorize(n)
	sum = 0
	for factor in factors:
		sum += factor
	if sum > n:
		return True
	else:
		return False
print(factorize(4))
print(isAbundant(4))


def FindAbundantNumberbleow(n):
	result = []
	for i in range(12,n+1):
		if isAbundant(i):
			result.append(i)
	return result

#可以先生成一个小于28123的表格，从这个表格中寻找特定的数字
Abundant_list = FindAbundantNumberbleow(1000)
newsum = 0
for i in range(24,100):
	trial = 0
	for j in range(1,i+1):
		if j in Abundant_list and (i-j) in Abundant_list:
			print("%d = %d+%d"%(i,j,i-j))
			trial +=1
			break		
	if trial == 0:
		print("%d cannot be the sum of two abundant numbers"%i)
		newsum += i
print(newsum)


#这种速度太慢了，每次都要重新找盈数。越往后时间越多，

#全部检查一遍，如果没有再输出的条件语句不熟悉
sum = 0
for num in range(24,100):
	trial = 0
	for i in range(1,num):
		if isAbundant(i) and isAbundant(num-i):
			#print(num,end="=")
			#print("%d + %d"%(i,num-i))
			trial += 1
		else:
			pass
	if trial ==0:
		print("%d cannot be the sum of two abundant numbers"%num)
	sum += num
print(sum)
