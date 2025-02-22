'''
Author: bddk
Date: 2024-02-27 11:11:07
LastEditors: bddk
LastEditTime: 2024-02-27 11:36:25
'''
add = []
query = []
IndexList = []

n, m = map(int, input().split())


for i in range(n):
    add.append(list(map(int, input().split())))
    IndexList.append(add[i][0])

for i in range(m):
    query.append(list(map(int, input().split())))
    IndexList.append(query[i][0])
    IndexList.append(query[i][1])

IndexList.sort()
IndexList = list(set(IndexList))

num = [0] * (len(IndexList)+1)
s = [0]*(len(IndexList)+1)


def find(x):
    l = 0
    r = len(IndexList)-1
    while l < r:
        mid = (l+r)//2
        if IndexList[mid] >= x:
            r = mid
        else:
            l = mid + 1
    return r + 1


for i in range(len(add)):
    x = find(add[i][0])
    num[x] += add[i][1]

for i in range(len(num)):
    s[i] = s[i - 1] + num[i]

for i in range(len(query)):
    l = find(query[i][0])
    r = find(query[i][1])
    print(s[r] - s[l - 1])
