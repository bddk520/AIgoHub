N = 110

f = [0] * N
g = [0] * N

a = []

n = int(input())

a = [0] + list(map(int, input().split()))

for i in range(1, n + 1):
    f[i] = 1
    for j in range(1, i):
        if a[i] > a[j]:
            f[i] = max(f[i], f[j] + 1)

for i in range(n, 0, - 1):
    g[i] = 1 
    for j in range(n, i, -1):
        if a[i] > a[j]:
            g[i] = max(g[i], g[j] + 1)
res = 0
for i in range(1, n + 1):
    res = max(res, f[i] + g[i] - 1)

print(n - res)
