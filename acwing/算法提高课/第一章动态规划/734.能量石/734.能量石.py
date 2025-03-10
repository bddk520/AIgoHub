N = 10000 + 5

f = [float("-inf")] * N
f[0] = 0


class stone:
    def __init__(self, s, e, l):
        self.s = s
        self.e = e
        self.l = l

    def __lt__(self, stone):
        return self.s * stone.l < stone.s * self.l


t = int(input())

for k in range(1, t + 1):
    f = [float("-inf")] * N
    f[0] = 0
    n = int(input())
    a = []
    m = 0
    for _ in range(n):
        s, e, l = map(int, input().split())
        a.append(stone(s, e, l))
        m += s
    a.sort()

    for i in range(n):
        s, e, l = a[i].s, a[i].e, a[i].l
        for j in range(m, s - 1, -1):
            f[j] = max(f[j], f[j - s] + e - (j - s) * l)

    res = max(f[:m + 1])

    print(f"Case #{k}: {res}")
