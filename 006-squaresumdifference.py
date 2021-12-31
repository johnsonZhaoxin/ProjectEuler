def squaresum(n):
    sum = 0
    for i in range(1,n+1):
        sum += i**2
    return sum

def sumsquare(n):
    sum = 0
    for i in range(1,n+1):
        sum+=i
    result = sum**2
    return result

diff = squaresum(100)-sumsquare(100)
print(diff)