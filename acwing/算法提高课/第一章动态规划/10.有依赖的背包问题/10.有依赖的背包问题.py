N = 110

e = [0] * N
ne = [0] * N
h = [-1] * N
v = [0] * N
w = [0] * N
f = [[0 for _ in range(N)]for _ in range(N)]
idx = 0
root = -1


def add(a, b):
    global idx
    e[idx] = b
    ne[idx] = h[a]
    h[a] = idx
    idx += 1


def dfs(u):
    global m
    for i in range(v[u], m + 1):
        f[u][i] = w[u]

    i = h[u]
    while i != -1:
        son = e[i]
        dfs(son)
        for j in range(m, v[u] - 1, -1):
            for k in range(0, j - v[u] + 1):
                f[u][j] = max(f[u][j], f[u][j - k] + f[son][k])

        i = ne[i]


n, m = map(int, input().split())

for i in range(1, n + 1):
    v[i], w[i], p = map(int, input().split())
    if p == -1:
        root = i
    else:
        add(p, i)

dfs(root)

print(f[root][m])
