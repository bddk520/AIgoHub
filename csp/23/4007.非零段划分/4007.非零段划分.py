N = 5 * int(1e5) + 10
M = int(1e5) + 10

cnt = [0] * N

n = int(input().strip())
a = list(map(int, input().strip().split()))
a = [v for i, v in enumerate(a) if i == 0 or v != a[i - 1]]

n = len(a)
a = [0] + a + [0]

for i in range(1, n + 1):
    x = a[i - 1]
    y = a[i]
    z = a[i + 1]
    if x > y and y < z:
        cnt[y] -= 1
    elif x < y and y > z:
        cnt[y] += 1

res = 0
SUM = 0
for i in range(M, 0, -1):
    SUM += cnt[i]
    res = max(res, SUM)

print(res)
