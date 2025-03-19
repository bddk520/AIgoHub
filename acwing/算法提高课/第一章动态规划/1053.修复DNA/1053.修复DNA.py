N = 1010

tr = [[0 for _ in range(4)] for _ in range(N)]
ne = [0] * N
dar = [0] * N
q = [0] * N
idx = 0
hh = 0
tt = - 1
f = [[float("inf") for _ in range(N)]for _ in range(N)]


def get(c):
    if c == "A":
        return 0
    if c == "T":
        return 1
    if c == "G":
        return 2
    if c == "C":
        return 3


def insert(s):
    global idx
    p = 0
    for i in range(len(s)):
        t = get(s[i])
        if tr[p][t] == 0:
            idx += 1
            tr[p][t] = idx
        p = tr[p][t]
    dar[p] = 1


def build():
    global tt, hh
    for i in range(4):
        if tr[0][i]:
            tt += 1
            q[tt] = tr[0][i]
    while hh <= tt:
        t = q[hh]
        hh += 1
        for i in range(4):
            p = tr[t][i]
            if p == 0:
                tr[t][i] = tr[ne[t]][i]
            else:
                ne[p] = tr[ne[t]][i]
                tt += 1
                q[tt] = p
                dar[p] |= dar[ne[p]]


T = 1

while True:

    n = int(input())

    if n == 0:
        break
    tr = [[0 for _ in range(4)] for _ in range(N)]
    ne = [0] * N
    dar = [0] * N
    idx = 0
    hh = 0
    tt = -1
    f = [[float("inf") for _ in range(N)]for _ in range(N)]
    f[0][0] = 0
    for i in range(n):
        s = input()
        insert(s)
    build()
    s = ' ' + input().strip() ##某位有空格注意
    m = len(s) - 1
    for i in range(len(s) - 1):
        for j in range(idx + 1):
            for k in range(4):
                cost = 1 if get(s[i + 1]) != k else 0
                p = tr[j][k]
                if dar[p] == 0:
                    f[i + 1][p] = min(f[i + 1][p], f[i][j] + cost)
    res = float("inf")
    for i in range(idx + 1):
        res = min(res, f[m][i])

    if res == float("inf"):
        print(f"Case {T}: -1")
        T += 1
    else:
        print(f"Case {T}: {res}")
        T += 1
