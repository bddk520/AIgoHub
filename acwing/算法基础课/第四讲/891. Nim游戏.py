res = 0

n = int(input())

arr = list(map(int,input().split()))

for i in range(n):
    res ^= arr[i]

if res == 0:
    print("No")
else:
    print("Yes")