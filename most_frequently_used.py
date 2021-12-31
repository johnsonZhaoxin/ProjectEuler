import math
import numpy as np
import itertools
from functools import lru_cache
import os
import string
import collections
import itertools


@lru_cache(maxsize=None)
#要找到一个简单省时间的算法
def isprime(n):
    if n == 1:
        return None
    elif n == 2 or n==3:
        return True
    else:
        for i in range(2,int(np.sqrt(n)+1)):
            if n%i == 0:
                return False
        return True


def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def seperate_num(num):
    digits = []
    [digits.append(int(i)) for i in str(num)]
    return digits


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def generate_num_from_list(list):
    num = ''
    for i in list:
        # print(str(i))
        num += str(i)
    return int(num)


@lru_cache(maxsize=None)
# 如果size是质数，是不包含在里面的。
def generate_prime_under1(size):
    result = []
    for i in range(2, size + 1):
        if isprime(i):
            result.append(i)
    return result


@lru_cache(maxsize=None)
# 这种方法不太行，速度反而比较慢
def generate_prime_under2(size):
    # 提前定义好第一个质数，但是该方法不能size小于2
    result = [2]

    # 开始遍历(2,size)之间的所有数：
    for i in range(2, size):
        # 用质数表里的数字去验证，这样会少比较多的运算次数
        for j in range(len(result)):
            count = 1
            if i % result[j] == 0:  # 能除得尽就不是质数
                count -= 1  # 控制器减去1
                break  # 停止后续循环
        if count == 1:  # 如果控制器保持不变，证明列表当中的数字都不是因子
            result.append(i)  # 可以将i这个数加入到质数表里面
    return result


def generate_prime_between(min_size, max_size):
    result = []
    for i in range(min_size, max_size + 1):
        if isprime(i):
            result.append(i)
    return result


def get_hypo(a, b, integer=True):
    err = 1e-7
    hypo = np.sqrt(a ** 2 + b ** 2)
    if integer:
        if hypo - int(hypo) < err:
            return hypo
        else:
            return None
        # print("斜边为整数,为%d"%(int(hypo)))
    else:
        # print("斜边不是整数,为%f" % (hypo))
        return hypo


def get_word_value(word):
    valueofcharacter = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
        "I": 9,
        "J": 10,
        "K": 11,
        "L": 12,
        "M": 13,
        "N": 14,
        "O": 15,
        "P": 16,
        "Q": 17,
        "R": 18,
        "S": 19,
        "T": 20,
        "U": 21,
        "V": 22,
        "W": 23,
        "X": 24,
        "Y": 25,
        "Z": 26,
        '"': 0,  # 因为读取的时候有点问题,会携带双引号。
    }
    sum = 0
    for char in word:
        sum += valueofcharacter[char]
    return sum


def prime_factorize(num):
    # res 是一个字典
    res, prim = collections.defaultdict(int), 2  # prime从2开始
    while num > 1:
        if num % prim == 0:
            num //= prim
            res[prim] += 1
        else:
            prim += 1
    return res


def delete_A_from_B(a_list, b_list):
    for item in a_list:
        b_list.remove(item)
    return b_list


def find_same_inAB(a_list, b_list):
    result = []
    for item in a_list:
        if item in b_list:
            result.append(item)
    return result


# 日期相关的函数
def daysinMonth(year, mon):
    if mon in [4, 6, 9, 11]:
        return 30
    elif mon in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mon == 2:
        if isleapyear(year):
            return 29
        else:
            return 28


def isleapyear(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False


def daysinYear(year):
    if isleapyear(year):
        return 366
    else:
        return 365


def daysbetween(year1, year2):
    # 这里指从year1 1.1 到 year2 1.1 完整的年份
    days = 0
    if year2 - year1 == 0:
        return days
    else:
        for i in range(year2 - year1):
            days += daysinYear(year1 + i)
        return days


def convertdays(datelist):
    # daylist=[year,month,day],最终结果是每个月的第几天。但是没有检查输入格式，报错的话没有考虑
    days = 0
    for month in range(1, datelist[1]):
        # print (daysinMonth(datelist[0],month))
        days += daysinMonth(datelist[0], month)
    return days + datelist[2]


def days_between_dates(datelist1, datelist2):
    # daylist=[year,month,day]，默认前面的时间小，后面的时间大
    day1 = convertdays(datelist1)
    day2 = convertdays(datelist2)

    # 相差多少年还要算一下
    wholedays = daysbetween(datelist1[0], datelist2[0])

    # 考虑一下要不要减去1的问题
    return wholedays - day1 + day2
