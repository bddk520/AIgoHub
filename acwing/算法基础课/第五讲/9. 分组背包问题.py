N = 110
v = [0] * N
w = [0] * N
f = [0] * N
n, m = map(int, input().split())

for _ in range(n):
    s = int(input())
    for j in range(1, s + 1):
        vi, wi = map(int, input().split())
        v[j] = vi
        w[j] = wi
    for j in range(m, 0, -1):
        for k in range(1, s + 1):
            if j >= v[k]:
                f[j] = max(f[j], f[j - v[k]] + w[k])

print(f[m])
