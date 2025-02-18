N = int(1e5) + 10

f = [int(-2e9)] * N

n = int(input())

arr = list(map(int,input().split()))

LEN = 0
for i in range(n):
    l = 0
    r = LEN
    while l < r:
        mid = (l + r + 1) // 2
        if f[mid] < arr[i]:
            l = mid
        else:
            r = mid - 1
    LEN = max(LEN,r + 1)
    f[r + 1] = arr[i]

print(LEN)