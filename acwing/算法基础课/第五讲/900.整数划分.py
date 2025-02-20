# N = 1010
# MOD = int(1e9) + 7

# f = [[0 for _ in range(N)] for _ in range(N)]

# f[1][1] = 1

# n = int(input())

# for i in range(2, n + 1):
#     for j in range(1, n + 1):
#         f[i][j] = (f[i - 1][j - 1] + f[i - j][j]) % MOD


# print(sum(f[n]) % MOD)
N = 1010
MOD = int(1e9) + 7

f = [[0 for _ in range(N)] for _ in range(N)]

n = int(input())

for i in range(1,n + 1):
    f[i][0] = 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        f[i][j] = f[i - 1][j] % MOD
        if j >= i:
            f[i][j] = (f[i][j] + f[i][j - i]) % MOD


print(f[n][n])
