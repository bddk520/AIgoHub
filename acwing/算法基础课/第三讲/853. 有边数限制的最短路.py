INF = float("inf")
N = 510


dist = [INF for _ in range(N)]
backup = [INF for _ in range(N)]


edges = []


def bellman_ford():
    dist[1] = 0
    for _ in range(k):
        backup = dist.copy()
        for i in range(m):
            a, b, c = edges[i]
            if dist[b] > backup[a] + c:
                dist[b] = backup[a] + c
    if dist[n] == INF:
        return "impossible"
    else:
        return dist[n]


n, m, k = map(int, input().split())

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

print(bellman_ford())
