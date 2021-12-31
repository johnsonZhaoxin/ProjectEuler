from most_frequently_used import *

ways = 0
# 先试试小一点的数字, 最后结果是840
for i in range(120,1000):
    count = 0
    for j in range(1,int(i/2)+1):
        for k in range(j,i-1-j):  #从j开始确保始终j,k,i-j-k从大到小的顺序
            if get_hypo(k,j,integer=True) == i-j-k:
                #print(j,k,i-j-k)
                count +=1
    print(count)
    ways = max(ways,count)
print(ways)