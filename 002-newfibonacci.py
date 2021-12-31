def fibonacci(n):
    n = int(n)
    if n > 2:
        result = fibonacci(n-1)+fibonacci(n-2)
    elif n == 2:
        result = 2
    elif n == 1:
        result = 1
    else:
        print("wrong number")
    return result

n = 1
seq =[]
while fibonacci(n) <=4e6:
    #print(fibonacci(n))
    seq.append(fibonacci(n))
    n += 1
print(seq)

sum = 0
for i in range(len(seq)):
    if seq[i]%2 == 0:
        sum += seq[i]
        print(sum)
print(sum)