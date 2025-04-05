N = int(1e5) + 10

n = int(input().strip())
a = list(map(int, input().strip().split())) + [0]

i = 0
while i <= n - i - 1:
    t = min(a[i], a[n - i - 1])
    a[i] -= t
    if i != n - i - 1:
        a[n - i - 1] -= t
    i += 1

cnt = 0
for i in range(n):
    cnt += a[i]
    a[i + 1] -= min(a[i], a[i + 1])

print(cnt)
