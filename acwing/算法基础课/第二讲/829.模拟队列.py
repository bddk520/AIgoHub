'''
Author: bddk
Date: 2024-02-29 15:47:48
LastEditors: bddk
LastEditTime: 2024-02-29 15:47:53
'''
queue = []

def push(x):
    queue.append(x)
def pop():
    queue.pop(0)
def empty():
    return len(queue) == 0
def query():
    return queue[0]

m = int(input())

for _ in range(m):
    op = input().split()
    if op[0] == 'push':
        push(int(op[1]))
    if op[0] == 'pop':
        pop()
    if op[0] == 'query':
        print(query())
    if op[0] == 'empty':    
        if empty():
            print('YES')
        else:
            print('NO')
            