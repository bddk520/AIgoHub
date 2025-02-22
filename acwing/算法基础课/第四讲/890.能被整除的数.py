p = []
n,m = map(int,input().split())

p = list(map(int,input().split()))

res = 0
for i in range(1,1 << m):
    t = 1
    cnt = 0
    for j in range(m):
        if i >> j & 1:
            if p[j] * t > n:
                t = -1
                break
            cnt += 1
            t = t * p[j]
    if t != -1:
        if cnt % 2:
            res += n // t
        else:
            res -= n // t

print(res)

    