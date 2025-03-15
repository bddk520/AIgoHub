N = 5 *int (1e5) + 10
s = [0] * N

t = int(input())

for _ in range(t):
    n = int(input())
    a = [0] + list(map(int, input().split()))
    res = float("inf")
    l = n // 2 + 1
    for i in range(1, n + 1):
        s[i] = s[i - 1] + a[i]
        if i >= l:
            res = min(res, s[i] - s[i - l])

    print(res, s[n] - s[0] - res)
