N = int(2 * 1e5) + 10
d = [0] * N
dd = [0] * N

n = int(input())

a = [0] + list(map(int, input().split()))


for i in range(1, n + 1):
    d[i] = a[i] - a[i - 1]

for i in range(1, n + 1):
    dd[i] = d[i] - d[i - 1]

res = 0
for i in range(1, n + 1):
    res += abs(dd[i])

print(res)
