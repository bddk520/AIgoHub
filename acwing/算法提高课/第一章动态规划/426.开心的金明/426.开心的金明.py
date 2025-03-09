N = 30000 + 10
M = 30

f = [0 for _ in range(N)]
w = [0] * N
v = [0] * N
n, m = map(int, input().split())

for i in range(1, m + 1):
    v[i], p = map(int, input().split())
    w[i] = v[i] * p

for i in range(1, m + 1):
    for j in range(n, v[i] - 1, -1):
        f[j] = max(f[j], f[j - v[i]] + w[i])

print(f[n])
