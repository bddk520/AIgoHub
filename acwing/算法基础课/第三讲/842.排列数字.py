'''
Author: bddk
Date: 2024-03-05 20:41:06
LastEditors: bddk
LastEditTime: 2024-03-05 20:41:11
'''
n = int(input())
p = [0]*(n)
flag = [0]*(n+1)


def dfs(u):
    if u == n:
        print(' '.join(map(str, p)))
        return
    for i in range(1, n+1):
        if not flag[i]:
            flag[i] = 1
            p[u] = i
            dfs(u + 1)
            flag[i] = 0


dfs(0)
