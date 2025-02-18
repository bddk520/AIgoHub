N = 1010

f = [0] * N

n = int(input())

arr = list(map(int, input().split()))

for i in range(n):
    f[i] = 1
    for j in range(i):
        if arr[j] < arr[i]:
            f[i] = max(f[i], f[j] + 1)

print(max(f))
