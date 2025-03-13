N = 20000 + 10
cnt = [[0 for _ in range(26)]for _ in range(26)]
st = [[0 for _ in range(26)]for _ in range(26)]
int_s = [0] * N


def update(l, r, v):
    global f, n
    l = max(0, l)
    r = min(n - 1, r)
    for i in range(l, r - 2 + 1):
        a = int_s[i]
        b = int_s[i + 1]
        c = int_s[i + 2]
        if a != b and b == c:
            cnt[a][b] += v
        if cnt[a][b] >= f:
            st[a][b] = 1


n, f = map(int, input().split())
s = input()
for i in range(len(s)):
    int_s[i] = ord(s[i]) - ord('a')

update(0, n - 1, 1)

for i in range(len(int_s)):
    t = int_s[i]
    update(i - 2, i + 2, -1)
    for j in range(26):
        if j != t:
            int_s[i] = j
            update(i - 2, i + 2, 1)
            update(i - 2, i + 2, -1)
    int_s[i] = t
    update(i - 2, i + 2, 1)

res = 0
for i in range(26):
    for j in range(26):
        if st[i][j]:
            res += 1

print(res)

for i in range(26):
    for j in range(26):
        if st[i][j]:
            print(chr(ord('a') + i) + chr(ord('a') + j) + chr(ord('a') + j))
