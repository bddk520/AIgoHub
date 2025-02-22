import heapq

heap = []
arr = []

n = int(input())

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: x[0])



for i in range(n):
    if len(heap) == 0 or heap[0] >= arr[i][0]:
        heapq.heappush(heap, arr[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, arr[i][1])

print(len(heap))
