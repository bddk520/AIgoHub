import heapq

N = int(1e5) + 10

arr = []

n = int(input())

arr = list(map(int, input().split()))


heapq.heapify(arr)

res = 0
now = 0
while len(arr) > 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    res += a + b

    heapq.heappush(arr, a + b)

print(res)
