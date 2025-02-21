def count(num, x):
    s = str(num)
    n = len(s)

    res = 0
    for i in range(not x, n):
        if i > 0:
            res += int(s[:i]) * pow(10, n - i - 1)
            if x == 0:
                res -= pow(10, n - i - 1)
        if int(s[i]) == x:
            if s[i + 1:]:
                res += int(s[i + 1:])
            res += 1
        elif int(s[i]) > x:
            res += pow(10, n - i - 1)

    return res


while True:
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break
    if a < b:
        a, b = b, a

    for i in range(10):
        if i < 9:
            print(count(a, i) - count(b - 1, i), end=" ")
        else:
            print(count(a, i) - count(b - 1, i))
