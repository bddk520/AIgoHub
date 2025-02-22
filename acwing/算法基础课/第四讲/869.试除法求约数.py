n = int(input())

def num(a):
    arr = []
    i = 1
    for i in range(1,(a // i) + 1):
        if a % i == 0:
            arr.append(i)
            if i != a // i:
                arr.append(a // i)
    arr.sort()
    print(" ".join(map(str,arr)))

for _ in range(n):
    a = int(input())
    num(a)
# def divide(n):
#     i = 1
#     f = []
#     while i <= n // i:
#         if n % i == 0:
#             f.append(i)
#             if i != n // i:
#                 f.append(n//i)

#         i += 1
#     f.sort()
#     return f

# n = int(input())
# while n:
#     n -= 1
#     a = int(input())
#     t = divide(a)
#     for i in t:
#         print(i,end=" ")
#     print()

