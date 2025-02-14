from collections import deque

N = 2000 + 10
M = 10000 + 10
INF = 0x3f3f3f3f # 注意这里不能用float("inf"),因为python中的inf无论减去多少个数，都是inf,不能到达负无穷，这道题需要d数组能减到负值

e = [0] * M
ne = [0] * M
h = [-1] * N
idx = 0
d = [INF] * N
cnt = [0] * N
st = [0] * N
w = [0] * M


def add(a, b, c):
    global idx
    e[idx] = b
    w[idx] = c
    ne[idx] = h[a]
    h[a] = idx
    idx += 1


def spfa():
    d[1] = 0
    q = deque()
    for i in range(1, n + 1):
        q.append(i)
        st[i] = 1 # 所有点入队列是因为从起点不一定能到负权边

    while q:
        t = q.popleft()
        st[t] = 0
        i = h[t]

        while i != -1:
            j = e[i]

            if d[j] > d[t] + w[i]:
                d[j] = d[t] + w[i]
                cnt[j] = cnt[t] + 1
                if cnt[j] >= n:
                    return "Yes"
                if st[j] == 0:
                    st[j] = 1
                    q.append(j)
            i = ne[i]

    return "No"


n, m = map(int, input().split())

for _ in range(m):
    a, b, c = map(int, input().split())
    add(a, b, c)


print(spfa())
