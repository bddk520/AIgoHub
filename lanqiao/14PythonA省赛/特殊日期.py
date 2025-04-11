import os
import sys

# 请在此输入您的代码

days = [0] + [31,28,31,30,31,30,31,31,30,31,30,31]

def getnum(a):
  res = 0
  while a:
    res += a % 10
    a //= 10
  return res

cnt = 0
for year in range(1900,9999 + 1):
  for month in range(1,12 + 1):
    day = days[month]
    if month == 2:
      if (year % 4 == 0and year % 100 != 0) or (year % 400 == 0):
        day = day + 1
    for i in range(1,day + 1):
        if getnum(year) == getnum(month) + getnum(i):
            cnt += 1

print(cnt)


    