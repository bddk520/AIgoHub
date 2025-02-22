N = int(1e5) + 10
M= int(2e5) + 10

p = [-1] * N

edges = []

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

n,m = map(int,input().split())

for _ in range(m):
    a,b,c = map(int,input().split())
    edges.append((a,b,c))

for i in range(1,n + 1):
    p[i] = i

edges.sort(key= lambda x:x[2])

res = 0
cnt = 0
for i in range(m):
    a,b,c = edges[i]
    a = find(a)
    b = find(b)
    if a!= b:
       p[a] = b
       res += c
       cnt += 1

if cnt == n - 1:
    print(res)
else:
    print("impossible")
        