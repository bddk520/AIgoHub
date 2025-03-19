from math import ceil, floor

N = 2 * int(1e5) + 5
rk = [0] * N

T = int(input())

for _ in range(T):
    n = int(input())
    h = [0] + list(map(int, input().split()))
    a = [0] + list(map(int, input().split()))

    t = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        rk[t[i] + 1] = i

    l = 0
    r = int(1e9)
    for i in range(1, n):
        A = h[rk[i]] - h[rk[i + 1]]
        B = a[rk[i + 1]] - a[rk[i]]

        if B > 0:
            r = min(r, ceil(A / B) - 1)
        elif B < 0:
            l = max(l, floor(A / B) + 1)
        elif A <= 0:
            r = -1
            break

    if l > r:
        l = -1
    print(l)
