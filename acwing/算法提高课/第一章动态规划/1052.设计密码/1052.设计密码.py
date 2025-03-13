N = 55
MOD = int(1e9) + 7
ne = [0] * N
f = [[0 for _ in range(N)] for _ in range(N)]
f[0][0] = 1 # 这里f[i][j]表示，已经生成i长度密码，且已经匹配了j个字符的方案，这里不同的i就是不同的状态


n = int(input())

s = ' ' + input()

m = len(s) - 1

j = 0
for i in range(2, m + 1):
    while j and s[i] != s[j + 1]:
        j = ne[j]
    if s[i] == s[j + 1]:
        j += 1
    ne[i] = j

for i in range(n):
    for j in range(m):
        for k in range(ord("a"), ord("z") + 1):
            u = j
            while u and chr(k) != s[u + 1]:
                u = ne[u]
            if chr(k) == s[u + 1]:
                u += 1
            if u < m:
                f[i + 1][u] = (f[i + 1][u] + f[i][j]) % MOD

res = sum(f[n][:m]) % MOD
print(res)

