N = 1010

a = [[0 for _ in range(N)] for _ in range(N)]
b = [[0 for _ in range(N)] for _ in range(N)]
c = [[0 for _ in range(N)] for _ in range(N)]

n,q = map(int,input().split())

res = 0
for _ in range(n):
    x,y,z = map(int,input().split())
    a[x][y] += 1
    if a[x][y] == n:
        res += 1
    b[y][z] += 1
    if b[y][z] == n:
        res += 1
    c[x][z] += 1
    if c[x][z] == n:
        res += 1
    print(res)
