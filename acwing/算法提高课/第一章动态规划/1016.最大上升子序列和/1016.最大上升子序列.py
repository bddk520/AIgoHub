N = 1010

a = []

f = [0] * N

n = int(input())

a = [0] + list(map(int, input().split()))


for i in range(1, n + 1):
    f[i] = a[i]
    for j in range(1, i):
        if a[i] > a[j]:
            f[i] = max(f[i], f[j] + a[i])


print(max(f))
