N = int(1e6) + 10
cnt = 0
l = [0] * N
r = [0] * N

n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    x = a[i]
    if l[x] == 0:
        cnt += 1
    l[x] += 1

res = 0
for i in range(n - 1, -1, -1):
    x = a[i]
    r[x] += 1
    l[x] -= 1
    if l[x] == 0:
        cnt -= 1
    if r[x] == 2:
        res += cnt
        if l[x] > 0:
            res -= 1
print(res)
