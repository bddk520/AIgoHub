N = 6000 + 10

f = [[0 for _ in range(2)] for _ in range(N)]

e = [0] * N
ne = [0] * N
h = [-1] * N
idx = 0

st = [0] * N
w = [0] * N


def add(a, b):
    global idx

    e[idx] = b
    ne[idx] = h[a]
    h[a] = idx
    idx += 1


def dfs(x):
    f[x][1] = w[x]

    i = h[x]

    while i != -1:

        t = e[i]

        dfs(t)

        f[x][1] += f[t][0]
        f[x][0] += max(f[t][0], f[t][1])

        i = ne[i]


n = int(input())

for i in range(1, n + 1):
    w[i] = int(input())

for _ in range(n - 1):
    a, b = map(int, input().split())
    add(b, a)
    st[a] = 1

root = 1
while st[root]:
    root += 1

dfs(root)
print(max(f[root][0], f[root][1]))
