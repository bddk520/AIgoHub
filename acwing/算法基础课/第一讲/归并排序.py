'''
Author: bddk
Date: 2024-02-13 20:49:59
LastEditors: bddk
LastEditTime: 2024-02-13 21:22:56
'''
# '''
# Author: bddk
# Date: 2024-02-13 20:49:59
# LastEditors: bddk
# LastEditTime: 2024-02-13 21:09:41
# '''
n = int(input())
arr = list(map(int, input().split()))


def merge(left, right):
    tmp = []
    l, r = len(left), len(right)
    i = j = 0
    while i < l and j < r:
        if left[i] <= right[j]:
            tmp.append(left[i])
            i += 1
        else:
            tmp.append(right[j])
            j += 1
    while i < l:
        tmp.append(left[i])
        i += 1
    while j < r:
        tmp.append(right[j])
        j += 1
    return tmp


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

result = merge_sort(arr)


print(' '.join(map(str,result)))

