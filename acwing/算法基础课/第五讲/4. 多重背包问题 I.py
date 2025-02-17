N = 110

f = [0 for _ in range(N)]

n, m = map(int, input().split())

for i in range(1, n + 1):
    vi, wi, si = map(int, input().split())
    for j in range(m, 0, -1):
        k = 1
        while k <= si and  j >= vi * k:
            f[j] = max(f[j], f[j - k * vi] + k * wi)
            k += 1

print(f[m])
