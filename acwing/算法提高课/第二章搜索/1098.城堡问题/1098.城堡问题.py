from queue import Queue

N = 55

st = [[0 for _ in range(N)] for _ in range(N)]

d = [[0, -1], [-1, 0], [0, 1], [1, 0]]

g = []


def bfs(x, y):
    q = Queue()
    q.put((x, y))
    st[x][y] = 1
    res = 1
    while q.empty() != True:
        cur_x, cur_y = q.get()

        for i in range(4):
            if g[cur_x][cur_y] >> i & 1:
                continue
            new_x = cur_x + d[i][0]
            new_y = cur_y + d[i][1]
            if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n and st[new_x][new_y] == 0:
                q.put((new_x, new_y))
                st[new_x][new_y] = 1
                res += 1

    return res


m, n = map(int, input().strip().split())

for _ in range(m):
    g.append(list(map(int, input().strip().split())))

cnt = 0
res = 0
for i in range(m):
    for j in range(n):
        if st[i][j] == 0:
            cnt += 1
            res = max(res, bfs(i, j))

print(cnt)
print(res)
