def sequence(n):
    if n%2 == 0:
        return n/2
    elif n%2 == 1 and n!=1:
        return 3*n+1
    else:
        return False


length = 0
start = 0
for i in range(2,1000000):
    list = []
    list.append(i)
    start = i
    while list[-1]:
        list.append(sequence(i))
        i = sequence(i)
    #print("初始值为%d是，数列有%d项"%(start,len(list)-1))
    #print(list)
    if len(list)>length:
        length = len(list)
        max = list[0]
print (length-1,max)