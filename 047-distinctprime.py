from most_frequently_used import prime_factorize

size=100000000000000000
i=21
while i<size:
    if len(prime_factorize(i+3))<4: i+=4
    elif len(prime_factorize(i+2))<4: i+=3
    elif len(prime_factorize(i+1))<4: i+=2
    elif len(prime_factorize(i))<4: i+=1
    else:
        print(i,prime_factorize(i))
        print(i+1,prime_factorize(i+1))
        print(i+2,prime_factorize(i+2))
        print(i+3,prime_factorize(i+3))
        break