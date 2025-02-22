'''
Author: bddk
Date: 2024-03-15 10:52:36
LastEditors: bddk
LastEditTime: 2024-03-15 11:15:31
'''
from collections import deque

N = 105
d = [[-1]*N for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
g = [list(map(int,input().split())) for _ in range(n)]

def bfs():
    q = deque()
    q.append((1,1))
    d[1][1] = 0
    while q:
        x, y = q.popleft()
        if x == n and y == m:
            break
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if a >= 1 and a <= n and b >= 1 and b <= m and d[a][b] == -1 and g[a - 1][b - 1] == 0:
                d[a][b] = d[x][y] + 1
                q.append((a, b))

bfs()
print(d[n][m])