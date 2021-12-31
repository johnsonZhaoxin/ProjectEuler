import numpy as np
def pentagon(n):
    return int(n*(3*n-1)/2)

def judge_pentagon(num):
    #换一种思路，求根公式当中整形
    if (1+(24*num+1)**0.5)%6==0:
        return True
    return False

#todo 有个前提，一定是sequence比较靠近的时候，才会使D比较小
flag = True
i = 2
while flag:
    for j in range(1,i):
        sum = pentagon(i)+pentagon(j)
        difference = pentagon(i)-pentagon(j)
        #print (sum,difference)
        if judge_pentagon(sum) and judge_pentagon(difference):
            #print(i,j)
            print(i,j)
            flag = False
            diff= difference
            break
    # 循环当中的 i+=1的位置真的很烦啊
    i += 1
print(diff)

#5482660 第1020项和第2167项
