# from math import gcd

# n = int(input())

# for _ in range(n):
#     a, b = map(int, input().split())
#     print(gcd(a,b))


def gcd(a,b):
    return gcd(b,a % b) if b != 0 else a

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    print(gcd(a,b))