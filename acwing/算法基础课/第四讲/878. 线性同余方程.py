x, y = 0, 0


def exgcd(a, b):
    global x, y
    if b == 0:
        x = 1
        y = 0
        return a
    d = exgcd(b, a % b)
    tmp = x
    x = y
    y = tmp - a // b * y

    return d


n = int(input())

for _ in range(n):
    a, b, m = map(int, input().split())
    d = exgcd(a, m)

    if b % d:
        print("impossible")
    else:
        print(b // d * x % m)
