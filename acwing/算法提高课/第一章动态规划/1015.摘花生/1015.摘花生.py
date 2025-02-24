N = 110

f = [[0 for _ in range(N)]for _ in range(N)]

t = int(input())

for _ in range(t):
    a = []
    f = [[0 for _ in range(N)]for _ in range(N)]
    r, c = map(int, input().split())
    for _ in range(r):
        a.append(list(map(int, input().split())))
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            f[i][j] = max(f[i - 1][j] + a[i - 1][j - 1], f[i][j])
            f[i][j] = max(f[i][j - 1] + a[i - 1][j - 1], f[i][j])
    print(f[r][c])
