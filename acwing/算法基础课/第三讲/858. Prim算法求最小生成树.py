N = 510
M = int(1e5) + 10

INF = float("inf")

g = [[INF for _ in range(N)] for _ in range(N)]
d = [INF] * N
st = [0] * N


# def prim():
#     res = 0
#     d[1] = 0
#     for j in range(n):
#         t = -1
#         for i in range(1, n+1):
#             if st[i] == 0 and (t == -1 or d[t] > d[i]):
#                 t = i

#         st[t] = 1

#         if j and d[t] == INF:
#             return "impossible"

#         res += d[t]

#         for i in range(1, n+1):
#             d[i] = min(d[i], g[t][i])

#     return res
def prim():
    res = 0
    d[1] = 0
    for j in range(n):
        t = -1
        for i in range(1, n+1):
            if st[i] == 0 and (t == -1 or d[t] > d[i]):
                t = i

        st[t] = 1

        if j and d[t] == INF:
            return "impossible"

        for i in range(1, n+1):
            if st[i] == 0:
                d[i] = min(d[i], g[t][i])
        res += d[t]
    return res


n, m = map(int, input().split())

for i in range(1, n + 1):
    g[i][i] = 0


for _ in range(m):
    a, b, c = map(int, input().split())
    g[a][b] = g[b][a] = min(g[a][b], c)

print(prim())
