V = 110
M = 110

f = [[0 for _ in range(M)] for _ in range(V)]

n, v, m = map(int, input().split())

for i in range(n):
    vi, mi, wi = map(int, input().split())
    for j in range(v, vi - 1, -1):
        for k in range(m, mi - 1, -1):
            f[j][k] = max(f[j][k], f[j - vi][k - mi] + wi)

print(f[v][m])
