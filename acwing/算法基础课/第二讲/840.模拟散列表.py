'''
Author: bddk
Date: 2024-03-05 13:12:21
LastEditors: bddk
LastEditTime: 2024-03-05 13:14:27
'''
# from collections import defaultdict

# dict = defaultdict(int)
# n = int(input())

# for _ in range(n):
#     op = input().split()
#     x = int(op[1])
#     if op[0] == 'I':
#         dict[x] += 1
#     if op[0] == 'Q':
#         if dict[x]:
#             print('Yes'
#                   )
#         else:
#             print('No')
N = 200003
null = 0x3f3f3f3f
h = [null] * N


def find(x):
    t = x % N
    while h[t] != null and h[t] != x:
        t += 1
        if t == N:
            t = 0
    return t


n = int(input())

for _ in range(n):
    op = input().split()
    x = int(op[1])
    if op[0] == 'I':
        h[find(x)] = x
    if op[0] == 'Q':
        if h[find(x)] != null:
            print('Yes'
                  )
        else:
            print('No')