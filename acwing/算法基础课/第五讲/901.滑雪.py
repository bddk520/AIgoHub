N = 310

choices = [[-1, 0], [0, 1], [1, 0], [0, -1]]

g = []
st = [[-1 for _ in range(N)] for _ in range(N)]

r, c = map(int, input().split())

g.append([])
for _ in range(r):
    g.append([0] + list(map(int, input().split())))

print(g)


def check(i, j):
    global r, c
    if i <= r and i >= 1 and j <= c and j >= 1:
        return True
    else:
        return False


def dfs(i, j):
    global r, c
    if st[i][j] != -1:
        return st[i][j]
    res = 1
    for choice in choices:
        if check(i + choice[0], j + choice[1]) and g[i][j] > g[i + choice[0]][j + choice[1]]:
            res = max(res, 1 + dfs(i + choice[0], j + choice[1]))
    st[i][j] = res
    return st[i][j]


def solution():
    global r,c
    max_depth = 1

    for i in range(1, r + 1):
        for j in range(1,c + 1):
            max_depth = max(max_depth,dfs(i,j))
    
    return max_depth

print(solution())
