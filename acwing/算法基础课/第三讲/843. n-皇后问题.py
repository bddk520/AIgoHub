'''
Author: bddk
Date: 2024-03-13 14:55:15
LastEditors: bddk
LastEditTime: 2024-03-13 15:28:47
'''
n = int(input())

N = 10
set = [['.'] * N for _ in range(N)]
row = [0] * N *2
dg = [0] * N *2
udg = [0] * N *2

def queen(i):
    if i == n:
        for i in range(n):
            for j in range(n):
                print(set[i][j],end = '')
            print()
        print()
        return
    for j in range(n):
        if row[j] == 0 and dg[i+j] == 0 and udg[i-j+n] == 0:
            row[j] = 1
            dg[i+j] = 1
            udg[i-j+n] = 1
            set[i][j] = 'Q'
            queen(i+1)
            row[j] = 0
            dg[i+j] = 0
            udg[i-j+n] = 0
            set[i][j] = '.'
        
queen(0)
