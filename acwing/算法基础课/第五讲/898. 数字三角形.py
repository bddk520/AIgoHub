N = 510

f = []

n = int(input())

for i in range(1, n + 1):
    f.append(list(map(int, input().split())))

for i in range(n - 2, -1, -1):
    for j in range(i + 1):
        f[i][j] = max(f[i + 1][j], f[i + 1][j + 1]) + f[i][j]

print(f[0][0])
