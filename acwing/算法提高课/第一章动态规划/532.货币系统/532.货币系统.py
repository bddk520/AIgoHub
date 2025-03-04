N = 25000 + 10

f = [0] * N

t = int(input())

for _ in range(t):
    f = [0] * N
    n = int(input())

    a = [0] + list(map(int,input().split()))
    a.sort()
    m = a[n]
    f[0] = 1
    res = 0
    for i in range(1,n + 1):
        if f[a[i]] == 0:
            res += 1
        for j in range(a[i],m + 1):
            f[j] |= f[j - a[i]]
        
    print(res)