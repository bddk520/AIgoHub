N = 55

f = [0] * N
g = [0] * N

a = []

ans = N


def dfs(u, su, sd):
    global ans
    if su + sd >= ans:
        return None
    if u == n:
        ans = min(ans, su + sd)
        return None

    k = 0
    while k < su and f[k] >= a[u]:
        k += 1
    if k < su:
        t = f[k]
        f[k] = a[u]
        dfs(u + 1, su, sd)
        f[k] = t  # 需要回溯
    else:
        f[k] = a[u]
        dfs(u + 1, su + 1, sd)

    k = 0
    while k < sd and g[k] <= a[u]:
        k += 1
    if k < sd:
        t = g[k]
        g[k] = a[u]
        dfs(u + 1, su, sd)
        g[k] = t  # 需要回溯
    else:
        g[k] = a[u]
        dfs(u + 1, su, sd + 1)


while True:
    n = int(input())
    if n == 0:
        break
    a = list(map(int, input().split()))
    f = [0] * N
    g = [0] * N
    ans = n

    dfs(0, 0, 0)
    print(ans)
