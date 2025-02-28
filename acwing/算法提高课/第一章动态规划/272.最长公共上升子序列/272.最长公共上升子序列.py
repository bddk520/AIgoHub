N = 3010

f = [[0 for _ in range(N)]for _ in range(N)]

a = []
b = []

n = int(input())

a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))

res = 0
for i in range(1, n + 1):
    maxv = 1
    for j in range(1, n + 1):
        f[i][j] = f[i - 1][j]

        if a[i] == b[j]:
            f[i][j] = max(f[i][j], maxv)
        if b[j] < a[i]:
            maxv = max(maxv, f[i - 1][j] + 1)


print(max(f[n]))
