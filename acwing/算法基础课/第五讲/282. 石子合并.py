N = 310

f = [[0 for _ in range(N)] for _ in range(N)]

s = [0] * N

n = int(input())

a = [0] + list(map(int, input().split()))


for i in range(n + 1):
    s[i] = s[i - 1] + a[i]

for LEN in range(2, n + 1):
    for i in range(1, n + 2 - LEN):
        j = i + LEN - 1
        f[i][j] = int(1e9)
        for k in range(i, j):
            f[i][j] = min(f[i][j], f[i][k] + f[k + 1][j] + s[j] - s[i - 1])

print(f[1][n])
