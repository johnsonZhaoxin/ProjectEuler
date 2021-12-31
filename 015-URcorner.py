#如果用编程语言的话就是动态规划问题
#如果使用数学上的排列组合问题就好了，总共要完成四步，在这四步当中，
#必须要有两步向上，两步向下，一次决定在第几步的时候走就可以了
#所以是4C2。动画的方式进行呈现

from itertools import permutations
right = 'right'
up ='up'
grid_length = 20
steps = []

for i in range(grid_length):
	steps.append(right)
	steps.append(up)

#print(steps)

paths = permutations(steps,40)
i = 0
for item in paths:
	#print (item)
	i +=1
print(i)
