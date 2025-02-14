'''
Author: bddk
Date: 2024-02-29 16:13:02
LastEditors: bddk
LastEditTime: 2024-02-29 16:26:34
'''
stack = []

n = int(input())
list = list(map(int, input().split()))


i = 0
while i < n:
    while (stack and stack[-1] >= list[i]):
        stack.pop()
    if not stack:
        print("-1", end=" ")
    else:
        print(stack[-1], end=" ")
    stack.append(list[i])

    i += 1
