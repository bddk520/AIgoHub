def exgcd(a, b):
    global x, y
    if b:
        d = exgcd(b, a % b)
        tmp = y
        y = x - (a // b) * y
        x = tmp
        return d
    else:
        x = 1
        y = 0
        return a


n = int(input())

x, y = 0, 0

for _ in range(n):
    a, b = map(int, input().split())
    exgcd(a, b)
    print(x, y)
