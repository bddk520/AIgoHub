'''
Author: bddk
Date: 2024-04-11 15:51:13
LastEditors: bddk
LastEditTime: 2024-04-13 00:05:06
'''
import os
import sys

n = int(input())
A = [0] + list(map(int,input().split()))
# m = int(input())
s = [0 for _ in range(n + 1)]
def chafen():
  for i in range(1,n + 1):
    s[i] = s[i - 1] + A[i]

chafen()
print(s)