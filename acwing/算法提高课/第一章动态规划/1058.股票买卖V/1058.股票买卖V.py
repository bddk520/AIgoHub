N = int(1e5) + 10

f = [[float("-inf") for _ in range(3)] for _ in range(N)]

n = int(input())
a = [0] + list(map(int, input().split()))
f[0][0] = 0
for i in range(1, n + 1):
    f[i][0] = max(f[i - 1][0], f[i - 1][2])
    f[i][1] = max(f[i - 1][1], f[i - 1][0] - a[i])
    f[i][2] = f[i - 1][1] + a[i]

print(max(f[n][0], f[n][2]))
