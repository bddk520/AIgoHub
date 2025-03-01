# 朴素写法
N = 105
M = 10000 + 10

f = [[0 for _ in range(M)]for _ in range(N)]

n, m = map(int, input().split())

a = [0] + list(map(int, input().split()))

for i in range(0,n + 1): ## 注意这里从0开始，从前0个物体在选择也是一种方案
    f[i][0] = 1

for i in range(1, n+1):
    for j in range(1, m + 1):
        f[i][j] = f[i - 1][j]
        if j >= a[i]:
            f[i][j] += f[i - 1][j - a[i]]

print(f[n][m])

# 优化
# N = 105
# M = 10000 + 10

# f = [0 for _ in range(M)]

# n, m = map(int, input().split())

# a = [0] + list(map(int, input().split()))

# f[0] = 1

# for i in range(1, n+1):
#     for j in range(m, 0,-1):
#         if j >= a[i]:
#             f[j] += f[j - a[i]]

# print(f[m])