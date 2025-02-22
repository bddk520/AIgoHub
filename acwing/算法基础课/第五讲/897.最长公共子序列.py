N = 1010


f = [[0 for _ in range(N)]for _ in range(N)]

n, m = map(int, input().split())
A = input()
B = input()

for i in range(n):
    for j in range(m):
        f[i][j] = max(f[i - 1][j], f[i][j - 1])
        if A[i] == B[j]:
            f[i][j] = max(f[i][j], f[i - 1][j - 1] + 1)

print(f[n - 1][m - 1])
