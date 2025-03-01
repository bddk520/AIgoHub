N = 16
M = 3000 + 5

f = [[0 for _ in range(M)] for _ in range(N)]

a = [0] * N

n, m = map(int, input().split())

for i in range(1, n + 1):
    a[i] = int(input())

for i in range(1, n + 1):
    f[i][0] = 1
    for j in range(1, m + 1):
        f[i][j] = f[i - 1][j]
        if j >= a[i]:
            f[i][j] += f[i][j - a[i]]
        
print(f[n][m])
