'''
Author: bddk
Date: 2024-02-17 23:28:08
LastEditors: bddk
LastEditTime: 2024-02-17 23:51:47
'''
n = int(input())
q = list(map(int, input().split()))
s = [0] * (int(1e6)+10)

res = 0

j = 0
for i in range(n):
    s[q[i]] +=1
    while j < i and s[q[i]] > 1:
        s[q[j]] -=1
        j +=1
    res = res if res > i - j +1  else i - j +1

print(res)
