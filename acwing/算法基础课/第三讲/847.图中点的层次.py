from queue import Queue

N = int(1e5) + 10
M = 2 * N
h = [-1] * N
e = [0] * M
ne = [-1] * M
idx = 0
q = Queue()
d = [-1] * N


def add(a, b):
    global idx
    e[idx] = b
    ne[idx] = h[a]
    h[a] = idx
    idx += 1


def bfs():
    q.put(1)
    d[1] = 0
    while not q.empty():
        t = q.get()

        i = h[t]
        while i != - 1:
            j = e[i]

            if d[j] == -1:
                d[j] = d[t] + 1
                q.put(j)
            i = ne[i]


n, m = map(int, input().split())

for _ in range(m):
    a, b = map(int, input().split())
    add(a, b)

bfs()

print(d[n])
