'''
Author: bddk
Date: 2024-02-14 20:03:40
LastEditors: bddk
LastEditTime: 2024-02-14 20:44:37
'''
n,m = map(int,input().split())
arr = [0] + list(map(int, input().split()))
s = [0] * (len(arr))

for i in range(1,n + 1):
    s[i] = s[i - 1] + arr[i]
while m > 0:
    m -= 1
    l,r = map(int,input().split())
    print(s[r] - s[l -1])
