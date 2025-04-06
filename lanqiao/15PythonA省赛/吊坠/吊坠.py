N = 205

n, m = map(int, input().strip().split())

a = []

g = [[0 for _ in range(N)] for _ in range(N)]
d = [float("-inf")] * N
st = [0] * N

for _ in range(n):
    a.append(input().strip())

for i in range(n):
    a[i] += a[i]

for i in range(n):

    sa = a[i]

    for j in range(i,n):
        f = [[0 for _ in range(2 * N)] for _ in range(2 * N)]
        sb = a[j]
        cnt = 0
        for k in range(2 * m):
            for z in range(2 * m):
                if (sa[k] == sb[z]):
                    f[k][z] = max(f[k - 1][z - 1] + 1, f[k][z])
                    cnt = max(cnt, f[k][z])
        g[i][j] = min(m, cnt)
        g[j][i] = min(m, cnt)

d[0] = 0

res = 0
for i in range(n):
    t = - 1
    for j in range(n):
        if st[j] == 0 and (t == - 1 or d[t] < d[j]):
            t = j
    st[t] = 1
    res += d[t]

    for j in range(n):
        d[j] = max(d[j], g[t][j])

print(res)
