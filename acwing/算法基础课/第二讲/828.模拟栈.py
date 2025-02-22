'''
Author: bddk
Date: 2024-02-28 22:44:06
LastEditors: bddk
LastEditTime: 2024-02-28 22:53:06
'''
stack = []


def push(x):
    stack.append(x)


def pop():
    return stack.pop()


def empty():
    if not stack:
        return 'YES'
    return 'NO'


def query():
    return stack[-1]


m = int(input())

while m:
    m -= 1
    op = input().split()
    if op[0] == 'push':
        push(op[1])
    if op[0] == 'pop':
        op()
    if op[0] == 'empty':
        print(empty())
    if op[0] == 'query':
        print(query())
