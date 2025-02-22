from queue import PriorityQueue

INF = float("inf")
N = int(1e6) + 10
e = [0]*N
ne = [0]*N
h = [-1]*N
st = [0]*N
w = [0]*N
idx = 0
d = [INF for _ in range(N)]


def add(a, b, c):
    global idx

    e[idx] = b
    ne[idx] = h[a]
    h[a] = idx
    w[idx] = c
    idx += 1



def dijkstra():

    d[1] = 0
    pq = PriorityQueue()
    pq.put((0, 1))

    while not pq.empty():
        dis, ver = pq.get()

        if st[ver]:
            continue
        st[ver] = 1

        t = h[ver]

        i = t
        while i != -1:
            j = e[i]

            if d[j] > d[ver] + w[i]:
                d[j] = d[ver] + w[i]
                pq.put((d[j], j))
            i = ne[i]
    if d[n] == INF:
        return -1
    else:
        return d[n]


n, m = map(int, input().split())

for _ in range(m):
    a, b, c = map(int, input().split())
    add(a, b, c)

print(dijkstra())
