N = 55

f = [[0 for _ in range(N)] for _ in range(N)]

n = int(input().strip())

a = [0] + list(map(int, input().strip().split()))

for LEN in range(3, n + 1):
    for i in range(1, n - LEN + 2):
        j = i + LEN - 1
        f[i][j] = float("inf")
        for k in range(i + 1, j):
            f[i][j] = min(f[i][j], f[i][k] + f[k]
                          [j] + a[i] * a[j] * a[k])

print(f[1][n])
