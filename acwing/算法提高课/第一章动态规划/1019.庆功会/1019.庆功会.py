N = 6000 + 10

f = [0] * N

n, m = map(int, input().split())

for i in range(n):
    v, w, s = map(int, input().split())
    for j in range(m, 0, -1):
        k = 1
        while k <= s and j >= k * v:
            f[j] = max(f[j], f[j - k * v] + k * w)
            k += 1

print(f[m])
