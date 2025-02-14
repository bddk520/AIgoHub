'''
Author: bddk
Date: 2024-02-28 23:09:16
LastEditors: bddk
LastEditTime: 2024-02-29 15:29:05
'''
nums = []
ops = []

pr = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}


def new_eval():
    a = nums.pop()
    b = nums.pop()
    op = ops.pop()

    if op == '+':
        nums.append(a + b)
    elif op == '-':
        nums.append(b - a)
    elif op == '*':
        nums.append(a * b)
    elif op == '/':
        nums.append(int(b / a))


str = input()

i = 0
while i < len(str):
    if str[i].isdigit():
        j = i
        num = 0
        while j < len(str) and str[j].isdigit():
            num = num*10 + int(str[j])
            j += 1
        nums.append(num)
        i = j - 1
    elif str[i] == '(':
        ops.append(str[i])
    elif str[i] == ')':
        while len(ops) > 0 and ops[-1] != '(':
            new_eval()
        ops.pop()
    else:
        if len(ops) > 0 and pr[str[i]] <= pr[ops[-1]]:
            new_eval()
        ops.append(str[i])
    i += 1

while len(ops) > 0:
    new_eval()
print(nums[-1])
