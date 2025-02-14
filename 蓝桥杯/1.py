import os
import sys

k = int(input())
s = input()

res = 0

def solve():
  
    global res
    l = len(s)
    if l < k:
        print(-1)


    l = l - l % k
    n = l // k

    for i in range(k):
        num = {}
        for j in range(i,l,k):
            if s[j] in num:
                num[s[j]] += 1
            else:
                num[s[j]] = 1
        res +=n - max([y for x,y in num.items()])
solve()
print(res)