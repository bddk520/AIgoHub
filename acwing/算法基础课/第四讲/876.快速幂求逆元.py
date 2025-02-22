def qmi(a, b, p):
    res = 1
    while b:
        if b & 1:
            res = res * a % p
        b >>= 1
        a = a * a % p
    return res


n = int(input())

for _ in range(n):
    a, p = map(int, input().split())

    if a % p:
        print(qmi(a, p-2, p))
    else:
        print("impossible")