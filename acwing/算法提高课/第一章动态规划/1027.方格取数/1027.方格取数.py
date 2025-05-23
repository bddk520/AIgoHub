N = 11

f = [[[0 for _ in range(N)]for _ in range(N)] for _ in range(2 * N)]
w = [[0 for _ in range(N)]for _ in range(N)]
n = int(input())

while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    w[a][b] = c

for k in range(2, 2 * n + 1):
    for i1 in range(1, n + 1):
        for i2 in range(1, n + 1):
            j1 = k - i1
            j2 = k - i2
            if j1 >= 1 and j1 <= n and j2 >= 1 and j2 <= n:
                t = w[i1][j1]
                if i1 != i2:
                    t += w[i2][j2]
                f[k][i1][i2] = max(f[k][i1][i2], f[k - 1][i1 - 1][i2 - 1] + t)
                f[k][i1][i2] = max(f[k][i1][i2], f[k - 1][i1 - 1][i2] + t)
                f[k][i1][i2] = max(f[k][i1][i2], f[k - 1][i1][i2 - 1] + t)
                f[k][i1][i2] = max(f[k][i1][i2], f[k - 1][i1][i2] + t)

print(f[2 * n][n][n])
