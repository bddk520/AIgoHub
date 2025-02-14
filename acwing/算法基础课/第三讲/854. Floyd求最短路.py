N = 210
M = 20000 + 10

INF = float("inf")

d = [[INF for _ in range(N)] for _ in range(N)]


def floyd():
    for k in range(1, n + 1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])


n, m, q = map(int, input().split())

for i in range(1,n + 1):
    d[i][i] = 0


for _ in range(m):
    a, b, c = map(int, input().split())
    d[a][b] = min(d[a][b], c)

floyd()


for _ in range(q):
    a, b = map(int, input().split())
    if d[a][b] == INF:
        print("impossible")
    else:
        print(d[a][b])
