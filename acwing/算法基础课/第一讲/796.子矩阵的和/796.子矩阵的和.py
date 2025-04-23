'''
Author: bddk
Date: 2024-02-14 21:09:08
LastEditors: bddk
LastEditTime: 2024-02-14 21:12:18
'''
n,m,q = map(int,input().split())
arr = [[0]*(m+1) for _ in range(n+1)]
s = [[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    arr[i] = [0] + list(map(int,input().split()))

for i in range(1,n+1):
    for j in range(1,m+1):
        s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + arr[i][j]

for _ in range(q):
    x1,y1,x2,y2 = map(int,input().split())
    print(s[x2][y2] - s[x1-1][y2] - s[x2][y1-1] + s[x1-1][y1-1])