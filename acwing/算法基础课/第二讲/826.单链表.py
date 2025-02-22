'''
Author: bddk
Date: 2024-02-28 14:21:08
LastEditors: bddk
LastEditTime: 2024-02-28 14:56:41
'''
N = 100010
head = -1
idx = 0

m = int(input())
op = []
e = [0]*N
ne = [0]*N

for _ in range(m):
    op.append(list(map(str, input().split())))


def add_to_head(x):
    global idx, head
    e[idx] = x
    ne[idx] = head
    head = idx
    idx += 1


def delete(k):
    global head
    if k == 0:  # 删除头节点
        head = ne[head]
    else:
        ne[k-1] = ne[ne[k-1]]  # 删除非头节点


def insert(k, x):
    global idx
    e[idx] = x
    ne[idx] = ne[k - 1]
    ne[k - 1] = idx
    idx += 1


for i in range(m):
    if op[i][0] == 'H':
        add_to_head(int(op[i][1]))
    if op[i][0] == 'D':
        delete(int(op[i][1]))
    if op[i][0] == 'I':
        insert(int(op[i][1]), int(op[i][2]))

while head != -1:
    print(e[head], end=' ')
    head = ne[head]
