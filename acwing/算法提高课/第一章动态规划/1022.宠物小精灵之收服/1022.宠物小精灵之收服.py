N = 1010
M = 510
K = 105

f = [[0 for _ in range(M)]for _ in range(N)]

n, m, k = map(int, input().split())

for i in range(1, k + 1):
    v1, v2 = map(int, input().split())
    for j in range(n, v1 - 1, -1):
        for z in range(m - 1, v2 - 1, -1):
            f[j][z] = max(f[j][z], f[j - v1][z - v2] + 1)

k = m - 1

while k > 0 and f[n][k - 1] == f[n][m - 1]:
    k -= 1

print(f[n][m - 1],m - k)
