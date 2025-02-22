def qmi(a, b, p):
    res = 1
    while b:
        if b & 1:
            res = res * a % p  # 注意这里不能写成res *= a % p，因为这样的话会先算a % p再 * res
        b >>= 1
        a = a * a % p
    return res


def C(a, b, p):
    if b > a:
        return 0
    res = 1
    j = a
    i = 1
    while i <= b:
        res = res * j % p
        res = res * qmi(i, p - 2, p) % p
        i += 1
        j -= 1
    return res


def lucas(a, b, p):
    if a < p and b < p:
        return C(a, b, p)
    return C(a % p, b % p, p) * lucas(a // p, b // p, p) % p


n = int(input())

for _ in range(n):
    a, b, p = map(int, input().split())
    print(lucas(a, b, p))
