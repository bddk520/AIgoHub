arr = []


def gauss():
    r = 0

    for c in range(n):

        t = r

        for i in range(r, n):
            if arr[i][c]:
                t = i
        if arr[t][c] == 0:
            continue

        arr[r], arr[t] = arr[t], arr[r]

        for i in range(r + 1, n):
            if arr[i][c]:
                for j in range(n, c - 1, -1):
                    arr[i][j] = arr[i][j] ^arr[r][j]
        r += 1

    if r < n:
        for i in range(r, n):
            if arr[i][n] == 1:
                return 0
        return 2

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            arr[i][n] = arr[i][n] ^ (arr[i][j] * arr[j][n])

    return 1


n = int(input())

for _ in range(n):
    arr.append(list(map(int, input().split())))

res = gauss()

if res == 0:
    print("No solution")
elif res == 2:
    print("Multiple sets of solutions")
elif res == 1:
    for i in range(n):
        print(arr[i][n])
