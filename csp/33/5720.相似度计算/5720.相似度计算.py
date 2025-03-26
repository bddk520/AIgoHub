n, m = map(int, input().strip().split())

a = set(input().strip().lower().split())
b = set(input().strip().lower().split())

print(len(a & b))
print(len(a | b))
