#todo 如何生成螺旋矩阵

# 首先解决问题，右上角的矩阵都是奇数的平方
def rightcorner(n):
    return n**2

# 然后四个边角与右上角分别是相差2，4，6这样
def sum_of_four_corners(n):
    UR = rightcorner(n)
    UL = UR +1-n
    DL = UL +1-n
    DR = DL +1-n
    return UR+UL+DL+DR

# 主程序循环，分别从3，5，7，9开始
sum = 1
for i in range(3,1002,2):
    sum += sum_of_four_corners(i)

print(sum)


