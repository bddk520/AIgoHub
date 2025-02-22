'''
Author: bddk
Date: 2024-03-04 18:33:06
LastEditors: bddk
LastEditTime: 2024-03-04 19:02:45
'''
n, m = map(int, input().split())

p = [i for i in range(n + 1)]



def find(x):
    while p[x] != x:
        p[x] = p[p[x]]
        x = p[x]
    return p[x]


for _ in range(m):
    op = input().split()
    a, b = int(op[1]), int(op[2])
    if op[0] == 'M':
        p[find(a)] = find(b)
    else:
        if find(a) == find(b):
            print('Yes')
        else:
            print('No')
