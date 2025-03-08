V = 20000 + 10

f = [0] * V
q = [0] * V
hh = 0
tt = -1

n, m = map(int, input().split())

for i in range(1, n + 1):
    v, w, s = map(int, input().split())
    g = f.copy()
    for j in range(v):
        hh = 0
        tt = -1
        for k in range(j, m + 1, v):
            if hh <= tt and q[hh] < k - s * v:
                hh += 1
            while hh <= tt and g[q[tt]] - (q[tt] - j) // v * w <= g[k] - (k - j) // v * w:
                tt -= 1
            tt += 1
            q[tt] = k
            f[k] = g[q[hh]] + (k - q[hh]) // v * w

print(f[m])
