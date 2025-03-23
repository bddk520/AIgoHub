n = int(input().strip())
b = [0] + list(map(int, input().strip().split()))

cur = 0
max_sum = 0
min_sum = 0
for i in range(1, n + 1):
    if i > 1:
        max_sum += b[i]
        if b[i] > cur:
            cur = b[i]
            min_sum += b[i]

    else:
        cur = b[i]
        max_sum += b[i]
        min_sum += b[i]

print(max_sum)
print(min_sum)
