'''
Author: bddk
Date: 2024-02-18 18:54:02
LastEditors: bddk
LastEditTime: 2024-02-18 19:11:13
'''
n,m,x = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))


i , j = 0, m -1
for i in range(n):
    while j < m and a[i] + b[j] > x:
        j -=1
    if a[i] + b[j] == x:
        break
    if a[i] + b[j] < x:
        continue

print(f"{i} {j}")