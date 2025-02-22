'''
Author: bddk
Date: 2024-02-28 19:01:14
LastEditors: bddk
LastEditTime: 2024-02-28 21:00:53
'''
N = 100010
m = int(input())
e = [0]*N
l = [0]*N
r = [0]*N

r[0] = 1
l[1] = 0
idx = 2


def insert(k, x):
    global idx
    e[idx] = x
    r[idx] = r[k]
    l[idx] = k
    l[r[k]] = idx
    r[k] = idx
    idx += 1


def remove(k):
    r[l[k]] = r[k]
    l[r[k]] = l[k]


while m:
    m -= 1
    op = list(map(str, input().split()))
    if op[0] == 'L':
        insert(0, int(op[1]))
    if op[0] == 'R':
        insert(l[1], int(op[1]))
    if op[0] == 'D':
        remove(int(op[1]) + 1)
    if op[0] == 'IL':
        insert(l[int(op[1])+1], int(op[2]))
    if op[0] == 'IR':
        insert(int(op[1])+1, int(op[2]))

while r[0] != 1:
    print(e[r[0]], end=' ')
    r[0] = r[r[0]]
