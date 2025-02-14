N = int(1e5) + 10
MOD = int(1e9) + 7

fact = [0] * N
infact = [0] * N


def qmi(a, b, p):
    res = 1
    while b:
        if b & 1:
            res *= a % p
        b >>= 1
        a *= a % p
    return res


fact[0], infact[0] = 1, 1
for i in range(1, N):
    fact[i] = (fact[i - 1] * i) % MOD
    infact[i] = (infact[i - 1] * (qmi(i, MOD - 2, MOD))) % MOD

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    print((fact[a] * infact[b] * infact[a - b]) % MOD)
