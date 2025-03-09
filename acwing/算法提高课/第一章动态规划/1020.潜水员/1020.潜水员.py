M = 25
N = 85

f = [[float("inf") for _ in range(N)] for _ in range(N)]
f[0][0] = 0

m, n = map(int, input().split())

k = int(input())

for _ in range(k):
    a, b, c = map(int, input().split())
    for i in range(m, -1, -1):
        for j in range(n, -1, -1):
            f[i][j] = min(f[i][j], f[max(0, i - a)][max(0, j - b)] + c)

print(f[m][n])
