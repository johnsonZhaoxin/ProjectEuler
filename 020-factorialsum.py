import math
def factorial(n):
	if n <0:
		print (error)
	elif n ==0:
		return 1
	elif n == 1:
		return 1
	else:
		return n*factorial(n-1)

largernum = factorial(100)
sum = 0
for digit in str(largernum):
	print(digit)
	sum += int(digit)

print(sum)