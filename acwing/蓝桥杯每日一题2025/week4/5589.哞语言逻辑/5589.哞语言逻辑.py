N = 2 * int(1e5) + 10

id = [0] * N
p = [0] * N
l = [0] * N
r = [0] * N
zeros = [0] * N
ones = [0] * N
cnt = 0

n, q = map(int, input().strip().split())

s = [" "] + input().strip().split()

for i in range(1, n + 1):
    if s[i] == "true" or s[i] == "or":
        p[i] = 1
    if i & 1:
        if i == 1 or p[i - 1]:
            cnt += 1
            l[cnt] = i
            r[cnt - 1] = i - 2
            if cnt >= 2:
                ones[cnt - 1] = ones[cnt - 2] + (0 if zeros[i - 2] else 1)
            zeros[i] = 0 if p[i] else 1

        else:
            zeros[i] = zeros[i - 2] + (0 if p[i] else 1)
        id[i] = cnt

r[cnt] = n
ones[cnt] = ones[cnt - 1] + (0 if zeros[n] else 1)

for _ in range(q):
    left, right, s = input().strip().split()
    left = int(left)
    right = int(right)
    res = 1 if s == "true" else 0
    lid = l[id[left]]
    rid = r[id[right]]
    a = ones[id[left] - 1] + ones[cnt] - ones[id[right]]
    b = zeros[rid] - zeros[right]
    if lid != left:
        b += zeros[left - 2]
    if res == int(a != 0 or b == 0) or res == int(a != 0):
        print("Y", end='')
    else:
        print("N", end='')
