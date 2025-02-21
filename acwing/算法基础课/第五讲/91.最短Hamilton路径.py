N = 20
M = 1 << N

w = []
f = [[float("inf") for _ in range(N)] for _ in range(M)]
f[1][0] = 0

n = int(input())

for _ in range(n):
    w.append(list(map(int, input().split())))

for i in range(1 << n):
    for j in range(n):
        if (i >> j) & 1:
            for k in range(n):
                if ((i - (1 << j)) >> k) & 1:
                    f[i][j] = min(f[i][j], f[i - (1 << j)][k] + w[k][j])

print(f[(1 << n) - 1][n - 1])
