'''
Author: bddk
Date: 2024-03-03 17:48:51
LastEditors: bddk
LastEditTime: 2024-03-03 18:01:17
'''
n = int(input())
p = ' ' + input()
m = int(input())
s = ' ' + input()
ne = [0] * (n + 1)


i = 2
j = 0
while i <= n:
    while j and p[i] != p[j + 1]:
        j = ne[j]
    if p[i] == p[j + 1]:
        j += 1
    ne[i] = j
    i += 1

i = 1
j = 0

while i <= m:
    while j and s[i] != p[j + 1]:
        j = ne[j]
    if s[i] == p[j + 1]:
        j += 1
    if j == n:
        print(i - n, end=' ')
        j = ne[j]
    i += 1
