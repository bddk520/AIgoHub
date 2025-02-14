'''
Author: bddk
Date: 2024-03-03 18:45:29
LastEditors: bddk
LastEditTime: 2024-03-03 19:16:50
'''
N = 2 * 10**4
n = int(input())
list = [[0] * 26 for i in range(N + 5)]
cnt = [0]*(N + 5)
idx = 0


def insert(str):
    global idx
    p = 0
    for i in range(len(str)):
        c = ord(str[i]) - ord('a')
        if list[p][c] == 0:
            idx += 1
            list[p][c] = idx 
        p = list[p][c]
    cnt[p] += 1

def query(str):
    p = 0
    for i in range(len(str)):
        c = ord(str[i]) - ord('a')
        if list[p][c] == 0:
            return 0
        p = list[p][c]
    return cnt[p]

for i in range(n):
    op = input().split()
    if op[0] == 'I':
        insert(op[1])
    if op[0] == 'Q':
        print(query(op[1]))
        
          