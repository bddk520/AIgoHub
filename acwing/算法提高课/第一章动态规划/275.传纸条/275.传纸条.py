N = 55

f = [[[0 for _ in range(N)]for _ in range(N)]for _ in range(2 * N)]
w = []

m,n = map(int,input().split())

w.append([])
for _ in range(m):
    w.append([0] + list(map(int,input().split())))

for k in range(2, n + m + 1):
    for i1 in range(1,m + 1):
        for i2 in range(1,m + 1):
            j1 = k - i1
            j2 = k - i2
            if j1 >= 1 and j1 <= n and j2 >= 1 and j2 <= n:
                t = w[i1][j1]
                if i1 != i2 or k == n + m or k == 2:
                    t += w[i2][j2]
                f[k][i1][i2] = max(f[k][i1][i2], f[k - 1][i1 - 1][i2 - 1] + t)
                f[k][i1][i2] = max(f[k][i1][i2], f[k - 1][i1 - 1][i2] + t)
                f[k][i1][i2] = max(f[k][i1][i2], f[k - 1][i1][i2 - 1] + t)
                f[k][i1][i2] = max(f[k][i1][i2], f[k - 1][i1][i2] + t)
                
print(f[n + m][m][m])
                

        
