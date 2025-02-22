N = int(1e5 + 10)
M = 2 * N

h = [-1] * N
e = [-1] * M
ne = [-1] * M
idx = 0
st = [0] * N
ans = N


def add(a, b):
    global idx
    e[idx] = b
    ne[idx] = h[a]
    h[a] = idx
    idx += 1


def dfs(u):
    global ans
    st[u] = 1

    size = 0
    SUM = 0

    i = h[u]
    while i != -1:
        j = e[i]
        if st[j]:
            i = ne[i]
            continue
        s = dfs(j)
        size = max(size, s)
        SUM += s

        i = ne[i]

    size = max(size, n - SUM - 1)
    ans = min(ans, size)

    return SUM + 1


n = int(input())
for _ in range(n - 1):
    a, b = map(int, input().split())
    add(a, b)
    add(b, a)

dfs(1)

print(ans)
