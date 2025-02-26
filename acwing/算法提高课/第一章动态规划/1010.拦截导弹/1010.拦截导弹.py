N = 1010

f = [0] * N
g = [0] * N

a = []


a = [0] + list(map(int, input().split()))

n = len(a) - 1

cnt = 0


for i in range(n, 0, -1):
    f[i] = 1
    for j in range(n, i, -1):
        if a[i] >= a[j]:
            f[i] = max(f[i], f[j] + 1)
    cnt = max(cnt, f[i])

print(cnt)

res = 0

for i in range(1, n + 1):
    k = 0
    while k < res and g[k] < a[i]:
        k += 1
    g[k] = a[i]
    if k >= res:
        res += 1

print(res)
