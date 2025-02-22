from queue import Queue

N = int(1e5)+10

INF = float("inf")

e = [0] * N
ne = [0] * N
h = [-1] * N
d = [INF] * N
idx = 0
w = [0] * N  # 标记这个点在不在队列中
st = [0] * N


def add(a, b, c):
    global idx
    e[idx] = b
    ne[idx] = h[a]
    h[a] = idx
    w[idx] = c
    idx += 1


def spfa():
    d[1] = 0
    q = Queue()
    q.put(1)
    st[1] = 1

    while not q.empty():
        t = q.get()
        st[t] = 0
        i = h[t]

        while i != -1:

            j = e[i]

            if d[j] > d[t] + w[i]:
                d[j] = d[t] + w[i]
                if st[j] == 0:
                    q.put(j)
                    st[j] = 1

            i = ne[i]

    if d[n] == INF:
        return "impossible"
    else:
        return d[n]


n, m = map(int, input().split())

for _ in range(m):
    a, b, c = map(int, input().split())
    add(a, b, c)

print(spfa())
