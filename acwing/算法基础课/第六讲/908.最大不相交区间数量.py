N = int(1e5) + 10

a = []

n = int(input())

for _ in range(n):
    a.append(list(map(int, input().split())))

a.sort(key=lambda x: x[1])

res = 0
ed = -2e9
for i in range(len(a)):
    if ed < a[i][0]:
        res += 1
        ed = a[i][1]

print(res)
