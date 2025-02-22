'''
Author: bddk
Date: 2024-02-19 17:24:41
LastEditors: bddk
LastEditTime: 2024-02-19 17:28:49
'''
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

j = 0
for i in range(m):
    if (a[j] == b[i]):
        j += 1
    if (j == n):
        break


if j == n:
    print("Yes"
          )
else:
    print("No")
