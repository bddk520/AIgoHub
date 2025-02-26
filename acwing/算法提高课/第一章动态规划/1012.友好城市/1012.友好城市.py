N = 5000 + 10

f = [0] * N
a = []

n = int(input())

for _ in range(n):
    a.append(list(map(int, input().split())))

a.sort(key=lambda x: x[0])

res = 0
for i in range(n):
    f[i] = 1
    for j in range(i):
        if a[i][1] > a[j][1]:
            f[i] = max(f[i], f[j] + 1)
            res = max(res, f[i])
print(res)
