def edit_distance(a, b):
    lena = len(a) - 1
    lenb = len(b) - 1
    f = [[0 for _ in range(lenb + 1)] for _ in range(lena + 1)]

    for i in range(lena + 1):
        f[i][0] = i
    for i in range(lenb + 1):
        f[0][i] = i

    for i in range(1, lena + 1):
        for j in range(1, lenb + 1):
            f[i][j] = min(f[i - 1][j] + 1, f[i][j - 1] + 1)
            if a[i] == b[j]:
                f[i][j] = min(f[i][j], f[i - 1][j - 1])
            else:
                f[i][j] = min(f[i][j], f[i - 1][j - 1] + 1)

    return f[lena][lenb]


n, m = map(int, input().split())

strs = []

for _ in range(n):
    strs.append(' ' + input())

for _ in range(m):
    c, limit = input().split()
    c = ' ' + c
    limit = int(limit)
    res = 0
    for i in range(n):
        if edit_distance(strs[i], c) <= limit:
            res += 1
    print(res)
