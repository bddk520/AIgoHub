'''
Author: bddk
Date: 2024-03-01 10:44:54
LastEditors: bddk
LastEditTime: 2024-03-01 11:02:24
'''
N = 100010
queue = [0]*N
head,tail = 0, -1
n, k = map(int, input().split())
list = list(map(int, input().split()))

head,tail = 0, -1
for i in range(n):
    while head <= tail and i - k + 1 > queue[0]:
        head += 1
    while head <= tail and list[i] <= list[queue[-1]]:
        tail -=1
    tail += 1
    queue[tail] = i
    if i >= k - 1:
        print(list[queue[0]], end=" ")

print()

queue = []
head,tail = 0, -1
for i in range(n):
    while head <= tail and i - k + 1 > queue[0]:
        head += 1
    while head <= tail and list[i] >= list[queue[-1]]:
        tail -= 1
    tail += 1
    queue[tail] = i
    if i >= k - 1:
        print(list[queue[0]], end=" ")
