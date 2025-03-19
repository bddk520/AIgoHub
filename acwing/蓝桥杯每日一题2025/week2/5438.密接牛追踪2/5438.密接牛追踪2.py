cnt = []

n = int(input())

s = input()

r = n
i = 0
while i < len(s):
    if s[i] == '0':
        i += 1
        continue
    j = i + 1
    while j <= n - 1 and s[j] == '1':
        j += 1
    c = j - i
    cnt.append(c)
    d = (c - 1) // 2
    if i == 0 or j == n:
        d = c - 1
    r = min(r, d)
    i = j

res = 0
for i in cnt:
    res += (i + 2 * r) // (2 * r + 1)
print(res)
