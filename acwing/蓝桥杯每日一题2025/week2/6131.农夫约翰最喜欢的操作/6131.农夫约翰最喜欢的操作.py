N = 2 * int(1e5) + 10

s = [0] * 2 * N

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    w = [-1] + list(map(int, input().split()))

    for i in range(1, n + 1):
        w[i] = w[i] % m

    w.sort()

    for i in range(1, n + 1):
        w.append(w[i] + m)

    for i in range(1, 2 * n + 1):
        s[i] = s[i - 1] + w[i]

    res = float("inf")
    for l in range(1, n + 1):
        r = l + n - 1
        p = (l + r) // 2
        left = (p - l + 1) * w[p] - (s[p] - s[l - 1])
        right = s[r] - s[p] - (r - p) * w[p]
        res = min(res, left + right)

    print(res)
