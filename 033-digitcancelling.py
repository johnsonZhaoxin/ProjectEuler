def speicalcancel(n, m):
    # n 和 m都是两位数
    numer1 = str(n)[0]
    numer2 = str(n)[1]

    deno1 = str(m)[0]
    deno2 = str(m)[1]
    # print(numer1,numer2,deno1,deno2)

    # todo 寻找四个当中相同的元素，分情况讨论，需要排除末尾为0，以及颠倒的情况,还有相同，但是最后为0的情况
    if int(deno1)*int(deno2)==0:
        return 0
    else:
        if numer1 == deno1:
            return int(numer2)/int(deno2)
        elif numer1 == deno2:
            return int(numer2)/int(deno1)
        elif numer2 == deno1:
            return int(numer1)/int(deno2)
        elif numer2 == deno2:
            return int(numer1)/int(deno1)



for num in range(10, 99):
    for deno in range(num + 1, 100):
        #print("%d/%d" % (num, deno))
        if num / deno == speicalcancel(num, deno):
            print("%d/%d" % (num, deno))