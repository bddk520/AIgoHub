N = 2 * int(1e5) + 10


t = int(input())

for _ in range(t):
    n = int(input())
    p = [[] for _ in range(N)]
    h = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        p[h[i]].append(i)
    cnt = 0

    for i in range(1, n + 1):
        for j in range(len(p[i]) - 1):
            if p[i][j + 1] - p[i][j] <= 2:
                cnt += 1
                print(i, end=" ")
                break
    if cnt == 0:
        print(-1, end="")
    print("")
