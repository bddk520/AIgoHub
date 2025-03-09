V = 1000 + 10
f = [0] * V


n, m = map(int, input().split())

for i in range(n):
    v, w, s = map(int, input().split())
    if s == 0:
        for j in range(v, m + 1):
            f[j] = max(f[j], f[j - v] + w)
    else:
        if s == -1:
            s = 1

        k = 1
        while s >= k:
            for j in range(m, k * v - 1, -1):
                f[j] = max(f[j], f[j - k * v] + k * w)
            s -= k
            k *= 2
        if s:
            for j in range(m, s * v - 1, -1):
                f[j] = max(f[j], f[j - s * v] + s * w)

print(f[m])
