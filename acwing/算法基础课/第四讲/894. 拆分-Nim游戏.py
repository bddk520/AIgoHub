N = 110
f = [-1] * N


def sg(x):
    global n
    S = set()
    if f[x] != -1:
        return f[x]
    for i in range(x):
        for j in range(i + 1):
            S.add(sg(i) ^ sg(j))
    return mex(S, x)


def mex(S, x):
    i = 0
    while True:
        if i not in S:
            f[x] = i
            return i
        i += 1


n = int(input())
a = list(map(int, input().split()))

res = 0

for i in range(n):
    res ^= sg(a[i])

print("Yes" if res != 0 else "No")
