'''
Author: bddk
Date: 2024-03-03 20:04:16
LastEditors: bddk
LastEditTime: 2024-03-03 20:38:01
'''
N = 3000000
n = int(input())
arr = list(map(int, input().split()))

son = [[0] * 2 for _ in range(N)]
idx = 0


def insert(x):
    global idx
    q = 0
    for i in range(30, -1, -1):
        u = x >> i & 1
        if son[q][u] == 0:
            idx += 1
            son[q][u] = idx
        q = son[q][u]


def query(x):
    global idx
    q = 0
    res = 0
    for i in range(30, -1, -1):
        u = x >> i & 1
        if son[q][~u]:
            res += 1 << i
            q = son[q][~u]
        else:
            q = son[q][u]
    return res



res = 0
for i in range(n):
    insert(arr[i])
    res = res if res > query(arr[i]) else query(arr[i])

print(res)
