N = int(1e5) + 10

f = [[0 for _ in range(2)] for i in range(N)]

t = int(input())

for _ in range(t):
    n = int(input())
    a = [0] + list(map(int, input().split()))

    f[0][0] = 0
    f[0][1] = float("-inf")

    for i in range(1, n + 1):
        f[i][0] = max(f[i - 1][0], f[i - 1][1])
        f[i][1] = f[i - 1][0] + a[i]

    print(max(f[n][0], f[n][1]))
