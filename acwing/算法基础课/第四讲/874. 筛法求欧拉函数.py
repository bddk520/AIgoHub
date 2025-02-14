N = int(1e6) + 10

phi = [0] * N
primes = [0] * N
st = [0] * N
cnt = 0

n = int(input())

phi[1] = 1
for i in range(2, n+1):
    if st[i] == 0:
        primes[cnt] = i
        cnt += 1
        phi[i] = i - 1
    j = 0

    while primes[j] * i <= n:
        st[primes[j] * i] = 1
        if i % primes[j] == 0:
            phi[primes[j] * i] = primes[j] * phi[i]
            break
        else:
            phi[primes[j] * i] = phi[i] * (primes[j] - 1)
        j += 1

print(sum(phi[1:n + 1]))
