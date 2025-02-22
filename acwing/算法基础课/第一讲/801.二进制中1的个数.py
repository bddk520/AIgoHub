'''
Author: bddk
Date: 2024-02-19 17:36:40
LastEditors: bddk
LastEditTime: 2024-02-19 17:36:44
'''
n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    res = 0
    while a[i]:
        if a[i] % 2 ==1:
            res += 1
        a[i] >>= 1

    print(res, end=" ")
