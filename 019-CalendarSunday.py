# 参考代码，但是不太对http://pe-cn.github.io/19/
from most_frequently_used import *
from datetime import* #datetime模块可以直接计算周一
#todo 我自己的想法是搞成了计算每一天，但是实际上没有必要，只要考虑每个月的开头是不是周日就好了



from collections import OrderedDict

months = OrderedDict( [("January",31),("February", 28),("March",31),
                       ("April", 30), ("May", 31), ("June", 30),
                       ("July", 31), ("August", 31), ("September", 30),
                       ("October", 31), ("November", 30), ("December", 31)] )

days = ['Tuesday','Wednesday', 'Thursday','Friday','Saturday', 'Sunday', 'Monday']

day = 0
sunday_count = 0

for year in range(1901,2001):
  leap = isleapyear(year)

  for m in months:
      dayName = days[day%7]
      if dayName == "Sunday":
          print(day)
          sunday_count += 1
      #print year, m, dayName
      day += months[m]
      if leap == True and m == "February":
          day += 1

print (sunday_count)
# print 171