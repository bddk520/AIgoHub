'''
Author: bddk
Date: 2024-03-04 19:03:16
LastEditors: bddk
LastEditTime: 2024-03-04 19:28:01
'''
'''
Author: bddk
Date: 2024-03-04 18:33:06
LastEditors: bddk
LastEditTime: 2024-03-04 19:02:45
'''
n, m = map(int, input().split())

p = [i for i in range(n + 1)]
cnt = [1] * (n + 1)


def find(x):
    while p[x] != x:
        p[x] = p[p[x]]
        x = p[x]
    return p[x]



for _ in range(m):
    op = input().split()

    if op[0] == 'C':
        a, b = int(op[1]), int(op[2])
        p_a = find(a)
        p_b = find(b)
        if p_a != p_b:
            p[p_a] = p_b
            cnt[p_b] += cnt[p_a]
    elif op[0] == 'Q1':
        a, b = int(op[1]), int(op[2])
        if find(a) == find(b):
            print('Yes')
        else:
            print('No')
    else:
        if op[0] == 'Q2':
            a = int(op[1])
            print(cnt[find(a)])
