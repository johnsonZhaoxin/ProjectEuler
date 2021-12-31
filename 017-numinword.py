import string

number_word = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety", 
    100: "hundred",
    #1000: "one thousand",#千位额外算
}

letter_count = 0
for i in range(1,1000):
    ge = int(i%10)
    shi = int((i%100-ge)/10)
    bai =int((i-10*shi-ge)/100)
    #print(bai,shi,ge)
    
    if bai ==0 and (shi == 1 or 0):  #一位数或者20以内的两位数
        word = number_word[i]
    elif bai==0 and (shi == 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9):
        word = number_word[shi*10]+" "+number_word[ge]
    elif bai !=0 and shi ==0 and ge ==0:
        word = number_word[bai]+" "+number_word[100]
    elif bai !=0 and shi==1:
        word = number_word[bai]+" "+number_word[100]+" and "+number_word[shi*10+ge]
    else:
        word = number_word[bai]+" "+number_word[100]+" and "+number_word[shi*10]+" "+number_word[ge]
    new_word = word.replace(" ","")        
    print ("%d用文字来写是%s"%(i,new_word))
    print(len(new_word))
    letter_count += len(new_word)
print(letter_count)
