N = 2 * int(1e5) + 10

n, q = map(int, input().strip().split())

c = list(map(int, input().strip().split()))

t = list(map(int, input().strip().split()))

a = [c[i] - t[i] for i in range(n)]

a.sort()


for _ in range(q):
    v, s = map(int, input().strip().split())
    l = 0
    r = n - 1
    while l < r:
        mid = (l + r + 1) // 2
        if (a[mid] <= s):
            l = mid
        else:
            r = mid - 1

    if a[l] <= s and n - l - 1 >= v:
        print("YES")
    else:
        print("NO")
