from most_frequently_used import get_word_value
def nC2(n):
    return int(0.5*n*(n+1))

def generate_triangle_seq(n):
    value = []
    for i in range(1,n+1):
        value.append(nC2(i))
    return value

triangle_seq_list = generate_triangle_seq(300) #这个其实不需要，只需要判断是不是三角数就行了

with open("p042_words.txt") as f:
    content = f.read()
f.close()

count = 0
for word in str(content).split(","): #先把content做str化，然后再以,分割。效率更高，022题可以解决更快。但是会带有双引号。
    word_value = get_word_value(word)
    if word_value in triangle_seq_list:
        print(word)
        count += 1

print(count)

