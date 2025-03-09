N = 1010
V = 1010

f = [[0 for _ in range(V)] for _ in range(N)]
v = [0] * N
w = [0] * N


n, m = map(int,input().split())

for i in range(1,n + 1):
    v[i],w[i] = map(int,input().split())

for i in range(n,0,-1):
    for j in range(0,m + 1):
        f[i][j] = f[i + 1][j]
        if j >= v[i]:
            f[i][j] = max(f[i][j],f[i + 1][j - v[i]] + w[i])

j = m

for i in range(1,n + 1):
    if j >= v[i] and f[i][j] == f[i + 1][j - v[i]] + w[i]:
        print(i,end=" ")
        j -= v[i]




