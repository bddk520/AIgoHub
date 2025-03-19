N = 2 * int(1e5) + 10
a = [0] * 2 * N

n, m = map(int, input().split())
s = input()

s = s + s

a = list(map(int, input().split()))

res = sum(a)

a.extend(a)

k = 0
while k < n and s[k] == s[k + 1]:
    k += 1

if k < n:
    i = k + 1
    while i <= n + k:
        j = i
        cnt = 0
        while j <= n + k and s[j] == s[i]:
            cnt += a[j]
            j += 1
        if s[i] == 'R':
            cnt -= a[j - 1]
        else:
            cnt -= a[i]
        res -= min(cnt, m)
        i = j - 1
        i += 1

print(res)
