# import math
# n, m = map(int, input().split())
# print(math.factorial(n) // math.factorial(n - m) // math.factorial(m))

N = 5000 + 10
primes = [0] * N
cnt = 0
st = [0] * N
SUM = [0] * N


def get_primes(n):
    global cnt
    for i in range(2, n + 1):
        if st[i] == 0:
            st[i] = 1
            primes[cnt] = i
            cnt += 1
        j = 0
        while primes[j] * i <= n:
            st[primes[j] * i] = 1
            if i % primes[j] == 0:
                break
            j += 1


def get(n, p):
    res = 0
    while n:
        res += n // p
        n //= p
    return res

def mul(a,b):
    c = []
    t = 0
    for i in range(len(a)):
        t += a[i] * b
        c.append(t % 10)
        t //= 10
    while t:
        c.append(t % 10)
        t //= 10
    return c

a, b = map(int, input().split())

get_primes(a)

for i in range(cnt):
    prime = primes[i]
    SUM[i] = get(a, prime) - get(b, prime) - get(a - b, prime)

res = []
res.append(1)
for i in range(cnt):
    for j in range(SUM[i]):
        res = mul(res,primes[i])

for i in range(len(res) - 1,- 1, -1):
    print(res[i],end="")

