import numpy as np

def natrual_sum(n):
	return (n-1)*n/2

def factorize(n):
	result = []
	for i in range(2,int(np.sqrt(n+1))):
		if n%i == 0:
			result.append(i)
			result.append(int(n/i))	
	
	result.append(1)

	factors = []

	for item in result:
		if item not in factors:
			factors.append(item)

	factors.sort()
	return factors

print(natrual_sum(12376))
print(factorize(natrual_sum(12376)))
print(len(factorize(natrual_sum(12376))))

# 主程序
#i = 28
#while len(factorize(natrual_sum(i)))<500:
#	i += 1

#print(i)