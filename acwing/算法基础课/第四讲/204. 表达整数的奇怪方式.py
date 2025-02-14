k1, k2 = 0, 0


def exgcd(a, b):
    global k1, k2

    if b == 0:
        k1 = 1
        k2 = 0
        return a
    else:
        d = exgcd(b, a % b)
        tmp = k1
        k1 = k2
        k2 = tmp - a // b * k2
        return d

x = 0
n = int(input())
m1, a1 = map(int, input().split())
for _ in range(n - 1):
    m2, a2 = map(int, input().split())
    d = exgcd(m1, m2)
    if (a2 - a1) % d:
        x = -1
        break
    k1 *= (a2 - a1) // d
    k1 = k1 % (m2 // d)

    x = k1 * m1 + a1

    a1 = x
    m1 = m1 // d * m2

if x != -1:
    x = a1 % m1
print(x)
