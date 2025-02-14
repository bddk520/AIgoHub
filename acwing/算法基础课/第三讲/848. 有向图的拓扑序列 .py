from queue import Queue

N = int(1e5) + 10

e = [0] * N
ne = [0] * N
h = [-1] * N
d = [0] * N
idx = 0
top = [0] * N


def add(a, b):
    global idx
    e[idx] = b
    ne[idx] = h[a]
    h[a] = idx
    idx += 1
    d[b] += 1


def topsort():
    cnt = 0
    q = Queue()
    for i in range(1, n + 1):
        if d[i] == 0:
            q.put(i)
    while not q.empty():
        t = q.get()
        top[cnt] = t
        cnt += 1

        i = h[t]
        while i != -1:
            j = e[i]
            d[j] -= 1
            if d[j] == 0:
                q.put(j)
            i = ne[i]
    return cnt == n


n, m = map(int, input().split())

for _ in range(m):
    a, b = map(int, input().split())
    add(a, b)

if topsort():
    print(" ".join(map(str, top[:n])))
else:
    print(-1)


