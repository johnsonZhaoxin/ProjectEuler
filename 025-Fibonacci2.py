from functools import lru_cache

# lru_cache的作用调用缓存
#被 lru_cache 修饰的函数在被相同参数调用的时候，后续的调用都是直接从缓存读结果，而不用真正执行函数。不需要重新计算
@lru_cache(maxsize=None)
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

n = 1
while len(str(fib(n))) < 1000:
    n += 1
print(n)


def fibonacci(n):
    n = int(n)
    result=0
    if n > 2:
        result = fibonacci(n-1)+fibonacci(n-2)
    elif n == 2:
        result = 1
    elif n == 1:
        result = 1
    else:
        print("wrong number")
    return result

#print(fibonacci(4782)) #最后答案，通过mma验证的， python好像超过了循环最大次数

# 我的程序，要改成1e1000，但是超出运行迭代次数了
i = 1
while fibonacci(i)<1e3:
	i+=1
print(i)
