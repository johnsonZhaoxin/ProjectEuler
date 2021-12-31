from itertools import combinations #用排列组合能够用更少的时间
import string
def is_palindromic(n):
    s = str(n)
    new_nums = []
    for i in range(len(s)):
        new_nums.append(s[-i-1])
    #print(new_nums)
    #print(list(s))

    if list(s) == new_nums:
        #print("%d is palindromic"%(n))
        return True
    else:
        #print("%d is NOT palindromic" % (n))
        return False

is_palindromic(1001)

result = 0
#for i in range(100,999):
#    for j in range(100,999): #用combination来写能够加快运行时间
for i,j in combinations(range(100,1000),2):
    product = i*j
    if is_palindromic(product) and product >=result:
        print(product)
        result = product
        print(i,j)