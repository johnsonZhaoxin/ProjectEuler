import os
import string
valueofcharacter ={
    "A":1,
    "B":2,
    "C":3,
    "D":4,
    "E":5,
    "F":6,
    "G":7,
    "H":8,
    "I":9,
    "J":10,
    "K":11,
    "L":12,
    "M":13,
    "N":14,
    "O":15,
    "P":16,
    "Q":17,
    "R":18,
    "S":19,
    "T":20,
    "U":21,
    "V":22,
    "W":23,
    "X":24,
    "Y":25,
    "Z":26,
}
# 还有必须按照字幕顺序排序

with open('p022_names.txt') as f:
    content = f.readlines()
f.close()
# 单独输出名字
content = str(content).split(",")

# 根据名称完成数字加减：
def nametonum(names):
    score = 0
    for char in str(names):
        #print(char,valueofcharacter[char])
        #score += valueofcharacter[char] if char in valueofcharacter else 0
        # 还有一种，用get函数
        score += valueofcharacter.get(str(char),0)
    return score

arranged_names = []
for i in range(len(content)):
    if i== 0:
        name = "MARY"
    elif i == 5162:
        name = "ALONSO"
    else:
        name = str(content[i]).replace('"', '')
    arranged_names.append(name)
arranged_names.sort()

max_score=0
for i in range(len(arranged_names)):
    score = (i+1)*nametonum(arranged_names[i])
    print ("第%d个人名为%s,分数为%d"%(i+1,arranged_names[i],score))
    max_score += score
print(max_score)