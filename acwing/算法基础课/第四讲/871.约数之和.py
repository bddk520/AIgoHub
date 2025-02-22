from collections import defaultdict
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
    if a > 1:
        primes[a] += 1

res = 1


for key, value in primes.items():
    t = 1
    for _ in range(1, value + 1):
        t = (t * key + 1) % MOD
    res = res * t % MOD

print(res)
