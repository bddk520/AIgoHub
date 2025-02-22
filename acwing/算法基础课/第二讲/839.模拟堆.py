'''
Author: bddk
Date: 2024-03-04 23:52:36
LastEditors: bddk
LastEditTime: 2024-03-05 00:13:47
'''
N = 100010
h = [0] * (N + 1)
ph = [0] * (N + 1)
hp = [0] * (N + 1)
cnt = m = 0


def swap(a, b):
    ph[hp[a]], ph[hp[b]] = ph[hp[b]], ph[hp[a]]
    hp[a], hp[b] = hp[b], hp[a]
    h[a], h[b] = h[b], h[a]


def up(x):
    while x//2 > 0 and h[x] < h[x//2]:
        swap(x, x//2)
        x = x//2


def down(x):
    u = x
    if x*2 <= cnt and h[u] > h[x*2]:
        u = x*2
    if x*2+1 <= cnt and h[u] > h[x*2+1]:
        u = x*2+1
    if u != x:
        swap(x, u)
        down(u)


n = int(input())

for _ in range(n):
    op = input().split()
    if op[0] == 'I':
        x = int(op[1])
        cnt += 1
        m += 1
        h[cnt] = x
        ph[m] = cnt
        hp[cnt] = m
        up(cnt)
    if op[0] == 'PM':
        print(h[1])
    if op[0] == 'DM':
        swap(1, cnt)
        cnt -= 1
        down(1)
    if op[0] == 'D':
        k = int(op[1])
        k = ph[k]
        swap(k, cnt)
        cnt -= 1
        up(k)
        down(k)
    if op[0] == 'C':
        k, x = int(op[1]), int(op[2])
        k = ph[k]
        h[k] = x
        up(k)
        down(k)
