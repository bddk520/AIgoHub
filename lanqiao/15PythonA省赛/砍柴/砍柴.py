N = int(1e5) + 10

a = [0] * N
st = [0] * N
f = [0] * N


primes = []


def get_primes():
    for i in range(2, n + 1):
        if st[i] == 0:
            primes.append(i)
        j = 0
        while primes[j] <= n // i:

            st[primes[j] * i] = 1
            if i % primes[j] == 0:
                break
            j += 1


t = int(input().strip())

for i in range(t):
    a[i] = int(input().strip())

n = max(a)

get_primes()

for i in range(2, n + 1):
    for prime in primes:
        if i >= prime:
            if f[i - prime] == 0:
                f[i] = 1

for i in range(t):
    print(1 if f[a[i]] == 1 else 0)
