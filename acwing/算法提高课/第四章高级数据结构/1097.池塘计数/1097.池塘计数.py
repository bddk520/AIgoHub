from queue import Queue

q = Queue()

N = 1010

g = []

st = [[0 for _ in range(N)] for _ in range(N)]

d = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]


def bfs(x, y):
    q.put((x, y))
    st[x][y] = 1
    while q.empty() != True:
        t = q.get()
        for i in range(len(d)):
            new_x = d[i][0] + t[0]
            new_y = d[i][1] + t[1]
            if (new_x >= 0 and new_x < n and new_y >= 0 and new_y < m):
                if g[new_x][new_y] == 'W' and st[new_x][new_y] == 0:
                    q.put((new_x, new_y))
                    st[new_x][new_y] = 1


n, m = map(int, input().strip().split())

for i in range(n):
    g.append(input().strip())

cnt = 0
for i in range(n):
    for j in range(m):
        if g[i][j] == 'W' and st[i][j] == 0:
            bfs(i, j)
            cnt += 1

print(cnt)
