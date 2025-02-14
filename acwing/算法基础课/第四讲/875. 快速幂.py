def qmi(a,b,p):
    res = 1
    while b:
        if b & 1:
            res = res * a % p
        b >>= 1
        a *= a % p
    return res

n =int(input())

for _ in range(n):
    a,b,p = map(int,input().split())
    print(qmi(a,b,p))
