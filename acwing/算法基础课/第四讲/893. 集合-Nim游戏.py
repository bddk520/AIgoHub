N = 110
M = 10010
f = [-1] * M


def sg(x):
    S = set()
    global m
    if f[x] != -1:
        return f[x]
    for i in range(m):
        if x >= s[i]:
            S.add(sg(x - s[i]))
    return mex(S, x)


def mex(S, x):
    i = 0
    while True:
        if i not in S:
            f[x] = i
            return i
        i += 1


m = int(input())

s = list(map(int, input().split()))

n = int(input())

h = list(map(int, input().split()))

res = 0
for i in range(n):
    res ^= sg(h[i])

print("Yes" if res != 0 else "No")
