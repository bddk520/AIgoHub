'''
Author: bddk
Date: 2024-02-14 21:17:08
LastEditors: bddk
LastEditTime: 2024-02-17 14:38:44
'''
n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
arr2 = [0] * (n+2)


def insert(l, r, c):
    arr2[l] += c
    arr2[r+1] -= c


for i in range(1, n+1):

    insert(i, i, arr[i])

while m > 0:
    m -= 1
    l, r, c = map(int, input().split())
    insert(l,r,c)


for i in range(1, n+1):
    arr2[i] += arr2[i-1]    

print(' '.join(map(str, arr2[1: -1])))
