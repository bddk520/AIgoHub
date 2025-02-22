'''
Author: bddk
Date: 2024-02-27 11:55:35
LastEditors: bddk
LastEditTime: 2024-02-27 19:29:20
'''
segs = []
n = int(input())
for i in range(n):
    segs.append(list(map(int, input().split())))


segs.sort(key=lambda x: x[0])


def merge(segs):
    res = []
    l, r = -1e9, -1e9
    for seg in segs:
        if r < seg[0]:
            if l != -1e9:
                res.append([l,r])
            l, r = seg[0], seg[1]
        else:
            r = r if r > seg[1] else seg[1]
    if l != -1e9:
        res.append([l, r])
    return res


segs = merge(segs)



print(len(segs))
