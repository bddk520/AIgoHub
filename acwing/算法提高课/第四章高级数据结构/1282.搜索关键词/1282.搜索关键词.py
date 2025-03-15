N = 10000 + 10
M = 55

tr = [[0 for _ in range(26)] for _ in range(N * M)]
cnt = [0 for _ in range(N * M)]
q = [0 for _ in range(N * M)]
ne = [0 for _ in range(N * M)]
hh = 0
tt = - 1
idx = 0

t = int(input())


def insert(s):
    global idx
    p = 0
    for i in range(len(s)):
        u = ord(s[i]) - ord('a')
        if tr[p][u] == 0:
            idx += 1
            tr[p][u] = idx
        p = tr[p][u]
    cnt[p] += 1


def build():
    global hh, tt
    for i in range(26):
        if tr[0][i]:
            tt += 1
            q[tt] = tr[0][i]

    while hh <= tt:

        t = q[hh]
        hh += 1
        for i in range(26):
            j = ne[t]
            c = tr[t][i]
            if c == 0:
                continue
            while j and tr[j][i] == 0:
                j = ne[j]
            if tr[j][i]:
                j = tr[j][i]
            ne[c] = j
            tt += 1
            q[tt] = c


for _ in range(t):
    tr = [[0 for _ in range(26)] for _ in range(N * M)]
    cnt = [0 for _ in range(N * M)]
    ne = [0 for _ in range(N * M)]
    hh = 0
    tt = - 1
    idx = 0
    n = int(input())
    for _ in range(n):
        s = input()
        insert(s)

    build()

    s = input()
    j = 0
    res = 0
    for i in range(len(s)):
        u = ord(s[i]) - ord('a')

        while j and tr[j][u] == 0:
            j = ne[j]
        if tr[j][u]:
            j = tr[j][u]

        p = j
        while p:
            res += cnt[p]
            cnt[p] = 0
            p = ne[p]

    print(res)
