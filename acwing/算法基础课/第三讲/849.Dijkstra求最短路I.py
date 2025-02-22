N = 510

INF = float("inf")

g = [[INF for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            g[i][j] = 0


d = [INF for _ in range(N)]

d[1] = 0

st = [0] * N


def dijkstra():
    for _ in range(n):
        t = -1
        for i in range(1, n + 1):
            if st[i] == 0 and (t == -1 or d[t] > d[i]):
                t = i
        st[t] = 1

        for i in range(1, n + 1):
            d[i] = min(d[i], d[t] + g[t][i])
    if d[n] == INF:
        return -1
    else:
        return d[n]


n, m = map(int, input().split())

for _ in range(m):
    a, b, c = map(int, input().split())
    g[a][b] = min(g[a][b], c)  # 存在重边，所以的当2个点之前第二次赋值时需要判断和前一次的赋值的大小


print(dijkstra())
