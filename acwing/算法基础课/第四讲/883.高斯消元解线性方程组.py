N = 110
arr = [[0 for _ in range(N)]for _ in range(N)]
eps = 1e-6


def gauss():
    r = 0

    for c in range(n):
        t = r
        for i in range(r, n):
            if abs(arr[i][c]) > abs(arr[t][c]):
                t = i

        if abs(arr[t][c]) < eps:
            continue

        # swap(arr[c])
        # for i in range(c, n + 1):
        #     arr[t][i], arr[r][i] = arr[r][i], arr[t][i]
        arr[t], arr[r] = arr[r], arr[t] 
        for i in range(n, c - 1, -1):
            arr[r][i] /= arr[r][c]
        for i in range(r + 1, n):
            if abs(arr[i][c]) > eps:
                for j in range(n, c - 1, -1):
                    arr[i][j] -= arr[i][c] * arr[r][j]
        r += 1

    if r < n:
        for i in range(r, n):
            if abs(arr[i][n]) > eps:
                return 0
        return 2
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            arr[i][n] -= arr[i][j] * arr[j][n]
    return 1


n = int(input())

for i in range(n):
    arr[i] = list(map(float, input().split()))

t = gauss()

if t == 0:
    print("No solution")
elif t == 2:
    print("Infinite group solutions")
elif t == 1:
    for i in range(n):
        print("{:.2f}".format(arr[i][n]))
