from math import fabs
N = 20
M = 1 << N
eps = 1e-8

f = [0] * M
q = [[0 for _ in range(2)] for _ in range(N)]
path = [[0 for _ in range(N)] for _ in range(N)]


t = int(input().strip())


def cmp(x, y):
    return fabs(x - y) < eps


for _ in range(t):
    n, m = map(int, input().strip().split())
    for i in range(n):
        x, y = map(float, input().strip().split())
        q[i][0] = x
        q[i][1] = y
    path = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(n):
        path[i][i] = 1 << i
        for j in range(n):
            x1 = q[i][0]
            y1 = q[i][1]
            x2 = q[j][0]
            y2 = q[j][1]
            if cmp(x1, x2):
                continue
            a = (y1 / x1 - y2 / x2) / (x1 - x2)
            b = y1 / x1 - a * x1

            if a > 0 or cmp(a, 0):
                continue

            state = 0
            for k in range(n):
                x3 = q[k][0]
                y3 = q[k][1]
                if (cmp(a * x3 * x3 + b * x3, y3)):
                    state += 1 << k
            path[i][j] = state

    f = [float("inf")] * M
    f[0] = 0
    for i in range((1 << n) - 1):
        x = 0
        for j in range(n):
            if (i >> j & 1) == 0:
                x = j
                break

        for j in range(n):
            f[i | path[x][j]] = min(f[i | path[x][j]], f[i] + 1)
    print(f[(1 << n) - 1])
