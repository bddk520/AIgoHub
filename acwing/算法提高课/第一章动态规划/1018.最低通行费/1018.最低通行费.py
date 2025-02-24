N = 110

f = [[float("inf") for _ in range(N)] for _ in range(N)]

w = []

n = int(input())

for _ in range(n):
    w.append(list(map(int, input().split())))


for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1 and j == 1:
            f[i][j] = w[i - 1][j - 1]
        if i > 1:
            f[i][j] = min(f[i][j], f[i - 1][j] + w[i - 1][j - 1])
        if j > 1:
            f[i][j] = min(f[i][j], f[i][j - 1] + w[i - 1][j - 1])

print(f[n][n])
