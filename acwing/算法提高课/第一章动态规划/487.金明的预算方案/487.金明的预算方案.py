M = 32010
N = 60
f = [0] * M
ms = [None] * N

sv = [[] for _ in range(N)]


m, n = map(int, input().split())

for i in range(1, n + 1):
    v, p, q = map(int, input().split())
    if q == 0:
        ms[i] = [v, v * p]
    else:
        sv[q].append([v, v * p])

for i in range(1, n + 1):
    if ms[i] is None:
        continue  # 跳过未被赋值的 ms[i]
    for u in range(m, -1, -1):
        for j in range(1 << len(sv[i])):
            v = ms[i][0]
            w = ms[i][1]
            for k in range(len(sv[i])):
                if j >> k & 1:
                    v += sv[i][k][0]
                    w += sv[i][k][1]
            if u >= v:
                f[u] = max(f[u], f[u - v] + w)

print(f[m])
