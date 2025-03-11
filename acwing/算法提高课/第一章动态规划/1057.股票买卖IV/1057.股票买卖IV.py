N = int(1e5) + 10
K = 110

f = [[float("-inf") for _ in range(2)] for _ in range(K)]

n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))


f[0][0] = 0

for i in range(1, n + 1):
    for j in range(k, -1, -1):
        f[j][0] = max(f[j][0], f[j][1] + a[i])#  f[j][0]和 f[j][1]的计算顺序不能反过来
        f[j][1] = max(f[j][1], f[j - 1][0] - a[i])

res = 0
for i in range(k + 1):
    res = max(res, f[i][0])
print(res)
