N = 105
M = 1 << 10

f = [[[0 for _ in range(M)]for _ in range(M)]for _ in range(2)]

state = []
cnt = [0] * M
g = [0] * N


def count(state):
    global m
    res = 0
    for i in range(m):
        if state >> i & 1:
            res += 1
    return res


n, m = map(int, input().split())

for i in range(1, n + 1):
    s = input()
    for j in range(m):
        if s[j] == 'H':
            g[i] += (1 << j)

for i in range(1 << m):
    if i & (i >> 1) == 0 and (i & (i >> 2)) == 0:
        state.append(i)
        cnt[i] = count(i)


for i in range(1, n + 1):
    for j in range(len(state)):
        for k in range(len(state)):
            a = state[j]
            b = state[k]
            f[i & 1][j][k] = 0
            if g[i] & a or g[i - 1] & b:
                continue
            for z in range(len(state)):
                c = state[z]
                if (a & b) or (a & c) or (b & c):
                    continue
                f[i & 1][j][k] = max(
                    f[i & 1][j][k], f[(i - 1) & 1][k][z] + cnt[a])

res = 0
for i in range(len(state)):
    for j in range(len(state)):
        a = state[i]
        b = state[j]

        res = max(res, f[n & 1][i][j])
print(res)
