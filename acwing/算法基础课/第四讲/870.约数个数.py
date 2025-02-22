from collections import defaultdict

N = 110
MOD = int(1e9) + 7
primes = defaultdict(int)

n = int(input())

for _ in range(n):
    a = int(input())
    i = 2

    while i * i <= a:

        while a % i == 0:
            a //= i
            primes[i] += 1
        i += 1
    if a > 1:  # 如果a本身是个质数
        primes[a] += 1

res = 1
for i in primes.values():
    res = int(res * (i + 1) % MOD)
print(res)
