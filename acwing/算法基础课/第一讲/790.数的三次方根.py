'''
Author: bddk
Date: 2024-02-14 19:06:35
LastEditors: bddk
LastEditTime: 2024-02-14 19:16:27
'''
n = float(input())
l, r = -100, 100
while ((r - l) > 1e-8):
    mid = (l+r)/2.0
    if (mid**3 >= n):
        r = mid
    else:
        l = mid + 1e-8
print(f"{l:.6f}")
