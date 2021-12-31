from itertools import permutations
values = [0,1,2,3,4,5,6,7,8,9]

data = list(permutations(values,len(values)))
#for i in range(int(1e6)):
#	print(data[i])
print(data[999999])
