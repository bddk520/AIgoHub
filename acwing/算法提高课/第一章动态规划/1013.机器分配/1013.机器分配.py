N = 20
v = [0] * N
w = [0] * N
f = [[0 for _ in range(N)] for _ in range(N)]
res = [0] * N
n, m = map(int, input().split())

a = []

for i in range(n):
    a.append([0] + list(map(int, input().split())))

for i in range(0, n):
    for j in range(m, -1, -1):
        f[i][j] = f[i - 1][j]
        for k in range(1, m + 1):
            if j >= k:
                f[i][j] = max(f[i][j], f[i - 1][j - k] + a[i][k])

print(f[n - 1][m])

j = m

way = [0] * N
for i in range(n - 1, -1, -1):
    for k in range(0, j + 1):
        if f[i][j] == f[i - 1][j - k] + a[i][k]:
            way[i] = k
            j -= k
            break

for i in range(n):
    print(i+ 1,way[i])
