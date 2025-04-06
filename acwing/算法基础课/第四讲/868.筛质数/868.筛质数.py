N = int(1e6 + 10)
primes = [0] * N
st = [0] * N
cnt = 0

n = int(input())

for i in range(2, n + 1):
    if st[i] == 0:
        primes[cnt] = i
        cnt += 1
    j = 0
    while primes[j] <= n // i:
        st[primes[j] * i] = 1
        if i % primes[j] == 0:
            break
        j += 1

print(cnt)