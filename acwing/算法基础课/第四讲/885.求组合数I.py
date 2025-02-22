N = 2000 + 10
MOD = int(1e9) + 7

c = [[0 for _ in range(N)] for _ in range(N)]

def init():
    for i in range(N):
        for j in range(i + 1):
            if j == 0:
                c[i][j] = 1
            else:
                c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % MOD

n = int(input())

init()

for _ in range(n):
    a,b = map(int,input().split())
    print(c[a][b])