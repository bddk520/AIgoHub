N = 510
M = int(1e5) + 10

e = [0] * M
ne = [0] * M
h = [-1] * N
idx = 0
st = [0] * N
match = [0] * N


def add(a, b):
    global idx
    e[idx] = b
    ne[idx] = h[a]
    h[a] = idx
    idx += 1


def find(u):
    i = h[u]
    while i != -1:
        j = e[i]

        if st[j] == 0: # 如果没有将 st[j] 设置为 1，那么在递归中，顶点 j 就有可能被重新访问，造成无限递归。
            st[j] = 1
            if match[j] == 0 or find(match[j]):
                match[j] = u
                return True

        i = ne[i]
    return False


n1, n2, m = map(int, input().split())

for _ in range(m):
    a, b = map(int, input().split())
    add(a, b)

res = 0 
for i in range(1, n1 + 1):

    for j in range(N):
        st[j] = 0

    if find(i):
        res += 1    

print(res)
