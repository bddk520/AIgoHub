'''
Author: bddk
Date: 2024-03-04 20:22:18
LastEditors: bddk
LastEditTime: 2024-03-04 20:22:22
'''
n, k = map(int, input().split())
p = [i for i in range(n+1)]
d = [0]*(n+1)


def find(x):
    # while p[x] != x:
    #     d[x] += d[p[x]]
    #     p[x] = p[p[x]]
    #     x = p[x]
    # return x
    if p[x] != x:
        t = find(p[x])
        d[x] += d[p[x]]
        p[x] = t
    return p[x]


res = 0

for _ in range(k):
    D, x, y = map(int, input().split())
    if x > n or y > n:
        res += 1
        continue
    if D == 1:
        px, py = find(x), find(y)
        if px == py and (d[x] - d[y])%3 != 0:
            res += 1
        elif px != py:
            p[px] = py
            d[px] = d[y] - d[x]
    else:
        px, py = find(x), find(y)
        if px == py and (d[x] - d[y] - 1)%3 != 0:
            res += 1
        elif px != py:
            p[px] = py
            d[px] = d[y] - d[x] + 1

print(res)