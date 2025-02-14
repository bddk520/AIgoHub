'''
Author: bddk
Date: 2024-03-04 22:55:27
LastEditors: bddk
LastEditTime: 2024-03-04 23:20:24
'''
# import heapq

# n,m = map(int,input().split() )
# arr = list(map(int,input().split()))

# heapq.heapify(arr)

# for _ in range(m):
#    print(heapq.heappop(arr),end=' ')

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

cnt = n

def down(x):
    u = x
    if x*2 <= cnt and arr[u] > arr[x*2]:
        u = x*2
    if x*2+1 <= cnt and arr[u] > arr[x*2+1]:
        u = x*2+1
    if u != x:
        arr[u], arr[x] = arr[x], arr[u]
        down(u)


for i in range(n//2, 0, -1):
    down(i)

for _ in range(m):
    print(arr[1], end=' ')
    arr[1] = arr[cnt]
    cnt -= 1
    down(1)
