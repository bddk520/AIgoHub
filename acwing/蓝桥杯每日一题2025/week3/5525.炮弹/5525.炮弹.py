from collections import defaultdict
N = int(1e5) + 10
entry = defaultdict()
q = []
v = []
st = [0] * N


n, s = map(int, input().split())

s = s - 1

for _ in range(n):
    qi, vi = map(int, input().split())
    q.append(qi)
    v.append(vi)

V = 1
flag = 1

cnt = 0
while s >= 0 and s < n:
    if q[s] and st[s] == 0:
        if v[s] <= V:
            cnt += 1
            st[s] = 1
    elif q[s] == 0:
        if entry.get(s) != None and entry[s] == V:
            break
        entry[s] = V
        V += v[s]
        flag = -flag

    s += flag * V

print(cnt)
