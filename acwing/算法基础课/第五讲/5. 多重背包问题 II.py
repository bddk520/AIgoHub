N = 2010

f = [0] * N

n, m = map(int, input().split())


for i in range(1, n + 1):
    goods = []
    v, w, s = map(int, input().split())
    k = 1
    while k <= s:
        s -= k
        goods.append((k * v, k * w))
        k *= 2
    if s > 0:
        goods.append((s * v, s * w))
    for good in goods:
        for j in range(m, good[0] - 1, - 1):
            f[j] = max(f[j], f[j - good[0]] + good[1])

print(f[m])
