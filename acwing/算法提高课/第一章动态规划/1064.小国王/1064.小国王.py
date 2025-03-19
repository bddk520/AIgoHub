N = 12
K = N * N
M = 1 << 10

f = [[[0 for _ in range(M)] for _ in range(K)]for _ in range(N)]
state = []
he = [[] for _ in range(M)]
cnt = [0] * M
n, k = map(int, input().split())


def check(state):
    if state >> 1 & state:
        return False
    return True


def count(state):
    res = 0
    for i in range(n):
        res += state >> i & 1
    return res


for i in range(1 << n):
    if check(i):
        state.append(i)
        cnt[i] = count(i)

for i in range(len(state)):
    for j in range(len(state)):
        a = state[i]
        b = state[j]
        if a & b == 0 and check(a | b):
            he[i].append(j)

f[0][0][0] = 1
for i in range(n + 2):
    for j in range(k + 1):
        for a in range(len(state)):
            for b in range(len(he[a])):
                if j >= cnt[state[a]]:
                    f[i][j][state[a]] += f[i - 1][j -
                                                  cnt[state[a]]][state[he[a][b]]]

print(f[n + 1][k][0])
