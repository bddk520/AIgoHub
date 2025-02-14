N = int(1e6) + 10
primes = [0] * N
st = [0] * N
cnt = 0


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


def get_fac_primes(n):
    global cnt
    tmpn = n
    for i in range(cnt):
        n = tmpn
        prime = primes[i]

        res = 0
        while n:
            res += n // prime
            n //= prime
        print(f"{prime} {res}")


n = int(input())
get_primes(n)
get_fac_primes(n)
