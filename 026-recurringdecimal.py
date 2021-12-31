import string

def calc_cycle(n):
	#别人的写法，不正确
    digits = []
    i=1
    while i!=0:
        cur_digit = int(i*10/n)
        if cur_digit in digits:
            print(digits[digits.index(cur_digit)::])
            break
        digits.append(cur_digit)
        i = i*10%n
    return digits


def find_recur(f):
	digits = str(f)[2:]
	for item in digits:
		print(item)

for i in range(1,1001):
	print(calc_cycle(1/i))
