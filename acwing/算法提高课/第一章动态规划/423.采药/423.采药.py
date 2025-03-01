M = 105
T = 1010

f = [[0 for _ in range(T)]for _ in range(M)]

a = []

t, m = map(int, input().split())

a.append([])
for _ in range(m):
    a.append(list(map(int, input().split())))

for i in range(1, m + 1):
    for j in range(1, t + 1):
        f[i][j] = f[i - 1][j]
        if j >= a[i][0]:
            f[i][j] = max(f[i][j], f[i - 1][j - a[i][0]] + a[i][1])

print(f[m][t])
