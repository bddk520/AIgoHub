
from collections import defaultdict

MOD = 1000000007


def qmi(a, b):
    res = 1
    while b:
        if b & 1:
            res = (res * a) % MOD
        b >>= 1
        a = (a * a) % MOD
    return res


def binary_search(arr, x):
    l = 0
    r = len(arr) - 1

    while l < r:
        mid = (l + r) >> 1
        if (arr[mid] >= x):
            r = mid
        else:
            l = mid + 1
    return l


def check(sr, sc, tr, tc):
    if (r[sr] > r[tr] or c[sc] > c[tc]):
        return False
    if r[sr] == r[tr] and sr != tr:
        return False
    if c[sc] == c[tc] and sc != tc:
        return False
    return True


n, m, t = map(int, input().strip().split())

r = [float("-inf")] + list(map(int, input().strip().split()))
c = [float("-inf")] + list(map(int, input().strip().split()))

cntr = defaultdict(int)
for i in range(1, n + 1):
    cntr[r[i]] += 1

cntc = defaultdict(int)
for i in range(1, m + 1):
    cntc[c[i]] += 1

r_sorted = (sorted(set(r)))
c_sorted = (sorted(set(c)))

fac = [1]
infac = [1]

for i in range(1, n + m + 1):
    fac.append(fac[i - 1] * i)
    infac.append(qmi(fac[i], MOD - 2))

s_r = [1]
in_s_r = [1]

for i in range(1, len(r_sorted)):
    s_r.append(s_r[i - 1] * cntr[r_sorted[i]] % MOD)
    in_s_r.append(qmi(s_r[i], MOD - 2))

s_c = [1]
in_s_c = [1]

for i in range(1, len(c_sorted)):
    s_c.append(s_c[i - 1] * cntc[c_sorted[i]] % MOD)
    in_s_c.append(qmi(s_c[i], MOD - 2))

for _ in range(t):
    sr, sc, tr, tc = map(int, input().strip().split())

    if check(sr, sc, tr, tc) == False:
        print(0)
    else:
        x1 = binary_search(r_sorted, r[sr])
        y1 = binary_search(c_sorted, c[sc])
        x2 = binary_search(r_sorted, r[tr])
        y2 = binary_search(c_sorted, c[tc])
        a = x2 - x1 + y2 - y1
        b = x2 - x1
        res = 1
        res = (res * fac[a]) % MOD
        res = (res * infac[b]) % MOD
        res = (res * infac[a - b]) % MOD

        if x2 != x1:
            res = (res * s_r[x2 - 1] * in_s_r[x1]) % MOD
        if y2 != y1:
            res = (res * (s_c[y2 - 1] * in_s_c[y1])) % MOD
        print(res)
