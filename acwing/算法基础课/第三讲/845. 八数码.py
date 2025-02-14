'''
Author: bddk
Date: 2024-03-15 15:05:07
LastEditors: bddk
LastEditTime: 2024-04-09 16:10:03
'''
from collections import deque


def bfs(state):
    end = '12345678x'
    q = deque()
    d = {state: 0}
    q.append(state)
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    while q:
        now = q.popleft()
        distance = d[now]
        if now == end:
            print(distance)
            return
        t = now.find('x')
        x = t // 3
        y = t % 3
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if a >= 0 and a < 3 and b >= 0 and b < 3:
                p = a * 3 + b
                next = list(now)
                next[t], next[p] = next[p], next[t]
                next = ''.join(next)
                if next not in d:
                    d[next] = distance + 1
                    q.append(next)
                next = list(now)
                next[t], next[p] = next[p], next[t]
                next = ''.join(next)
    print(-1)


n = input().split()
str = ''
for i in n:
    str += i

bfs(str)
