
N = int(1e5) + 10

arr = []

n = int(input())

arr = list(map(int, input().split()))

arr.sort()

res = 0

for i in range(n):
    res += arr[i] * (n - i - 1)

print(res)