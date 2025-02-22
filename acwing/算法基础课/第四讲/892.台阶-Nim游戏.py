res = 0
n = int(input())

arr = list(map(int,input().split()))

for i in range(n):
    if i % 2 == 0:
        res ^= arr[i]

if res:
    print("Yes")
else:
    print("No")