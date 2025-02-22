'''
Author: bddk
Date: 2024-03-05 13:25:11
LastEditors: bddk
LastEditTime: 2024-03-05 13:27:27
'''
N = 100010
P = 131
Q = 1 << 64
h = [0]*N
p = [0]*N

def find(l,r):
    return ((h[r]-h[l-1]*p[r-l+1])%Q)

n, m = map(int, input().split())
str = ' ' + input()

p[0] = 1
for i in range(1,n+1):
    p[i] = (p[i-1]*P)%Q
    h[i] = (h[i-1]*P+ord(str[i]))%Q

for _ in range(m):
    l1,r1,l2,r2 = map(int, input().split())
    if find(l1,r1) == find(l2,r2):
        print("Yes")
    else:
        print("No")
