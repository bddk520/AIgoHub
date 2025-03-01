N = 1010

f = [[0 for _ in range(N)]for _ in range(5)]

a = [0, 10, 20, 50, 100]

n = int(input())

 
for i in range(1, 5):
    f[i][0] = 1 
    for j in range(1, n + 1):
        f[i][j] = f[i - 1][j]
        if j >= a[i]:
            f[i][j] += f[i][j - a[i]]

print(f[4][n])
