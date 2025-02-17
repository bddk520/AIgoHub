# N = 1010
# V = N * [0]
# W = N * [0]
# f = [[0 for _ in range(N)] for _ in range(N)]

# n, v = map(int, input().split())

# for i in range(1, n + 1):
#     vi, wi = map(int, input().split())
#     V[i] = vi
#     W[i] = wi

# for i in range(1, n + 1):
#     for j in range(1, v + 1):
#         f[i][j] = f[i - 1][j]
#         if j >= V[i]:
#             f[i][j] = max(f[i][j], f[i - 1][j - V[i]] + W[i])

# print(f[n][v])
N = 1010
V = N * [0]
W = N * [0]
f = [0 for _ in range(N)]
n, v = map(int, input().split())

for i in range(1, n + 1):
    vi, wi = map(int, input().split())
    V[i] = vi
    W[i] = wi

for i in range(1, n + 1):
    for j in range(v, 0, -1):
        if j >= V[i]:
            f[j] = max(f[j], f[j - V[i]] + W[i])

print(f[v])
