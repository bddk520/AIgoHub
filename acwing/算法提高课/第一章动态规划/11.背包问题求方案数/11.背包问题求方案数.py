N = 1010
MOD = int(1e9) + 7

f = [[0 for _ in range(N)]for _ in range(N)]
g = [[0 for _ in range(N)]for _ in range(N)]
v = [0] * N
w = [0] * N

n, m = map(int, input().split())

for i in range(0, m + 1):
    g[0][i] = 1

for i in range(1, n + 1):
    vi, wi = map(int, input().split())
    v[i] = vi
    w[i] = wi
    for j in range(m, -1, -1):
        f[i][j] = f[i - 1][j]
        if j >= vi:
            if f[i][j] < f[i - 1][j - v[i]] + w[i]:
                f[i][j] = f[i - 1][j - v[i]] + w[i]
                g[i][j] = g[i - 1][j - v[i]]
            elif f[i][j] == f[i - 1][j - v[i]] + w[i]:
                g[i][j] = (g[i - 1][j - v[i]] + g[i - 1][j]) % MOD
            else:
                g[i][j] = g[i - 1][j]
        else:
            g[i][j] = g[i - 1][j]


print(g[n][m])
