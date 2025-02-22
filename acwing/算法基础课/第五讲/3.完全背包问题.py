# N = 1010

# w = [0] * N
# v = [0] * N
# f = [[0 for _ in range(N)]for _ in range(N)]


# n, m = map(int, input().split())

# for i in range(1, n + 1):
#     vi, wi = map(int, input().split())
#     v[i] = vi
#     w[i] = wi

# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         f[i][j] = f[i - 1][j]
#         if j >= v[i]:
#             f[i][j] = max(f[i][j], f[i][j - v[i]] + w[i])

# print(f[n][m])

N = 1010

w = [0] * N
v = [0] * N
f = [0 for _ in range(N)]

n, m = map(int, input().split())

for i in range(1, n + 1):
    vi, wi = map(int, input().split())
    v[i] = vi
    w[i] = wi

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if j >= v[i]:
            f[j] = max(f[j], f[j - v[i]] + w[i])

print(f[m])