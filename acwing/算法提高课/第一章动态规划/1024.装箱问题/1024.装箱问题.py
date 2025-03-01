V = 20000 + 10
N = 35

f = [[0 for _ in range(V)]for _ in range(N)]

a = []

v = int(input())
n = int(input())

a.append(0)
for _ in range(n):
    a.append(int(input()))

for i in range(1, n + 1):
    for j in range(1, v + 1):
        f[i][j] = f[i - 1][j]
        if j >= a[i]:
            f[i][j] = max(f[i][j], f[i - 1][j - a[i]] + a[i])

print(v - f[n][v])
