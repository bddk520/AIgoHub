a = []

n = int(input())

for _ in range(n):
    a.append(list(map(int,input().split())))

a.sort(key=lambda x:x[0] + x[1])

N = 50000 + 10
s = [0] * N


res = float("-inf")
SUM = 0
for i in range(n):
    w = a[i][0]
    s = a[i][1]
    res = max(res,SUM - s)
    SUM += w
print(res)