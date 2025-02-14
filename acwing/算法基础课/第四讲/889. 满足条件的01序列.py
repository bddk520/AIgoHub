MOD = int(1e9) + 7  # 卡特兰数


def qmi(a, b, p):
    res = 1
    while b:
        if b & 1:
            res = res * a % p
        b >>= 1
        a = a * a % p
    return res

n = int(input())

a, b = 2*n, n
res = 1

for i in range(a, a-b, -1):
    res = res * i % MOD

for i in range(1, b + 1):
    res = res * qmi(i, MOD - 2, MOD) % MOD

res = res * qmi(n + 1, MOD - 2, MOD) % MOD

print(res)
