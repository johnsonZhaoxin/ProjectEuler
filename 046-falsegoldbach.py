from most_frequently_used import *

#todo 质数表该有多大？
prime_list = generate_prime_under1(10000)
print(prime_list)


def false_goldbach(num):
    criteria = 0
    i = 0
    diff=10000 #一开始就定义好，让程序启动起来
    while diff >=2 and i<len(prime_list):
        xiaoprime = prime_list[i]
        diff = num - xiaoprime
        #print(diff)
        square = np.sqrt(diff/2)
        #print(square)
        if square-int(square) < 1e-7:
            print("%d=%d+2*%d^2"%(num,xiaoprime,square))
            criteria += 1
            break
        else:
            #print("%d doesn't work"%(xiaoprime))
            i+=1
    if criteria == 1:
        return True
    else:
        return False

#todo 不知道数据应该到多少
#最后答案5777。但是速度上面有点慢，生成质数表的方式太慢了。
guess = 33
while false_goldbach(guess):
    guess+=2