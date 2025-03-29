'''
Author: bddk
Date: 2024-02-13 21:31:51
LastEditors: bddk
LastEditTime: 2024-02-13 22:12:07
'''

n = int(input())
arr = list(map(int, input().split()))


def merge_sort(arr):
    if len(arr) <= 1:
        return 0,arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]   
    num_l,left =  merge_sort(left)
    num_r,right =  merge_sort(right)
    num_m,merge_arr = merge(left, right)

    return num_l+num_r+num_m,merge_arr

def merge(left, right):
    tmp = []
    num = 0
    i = j = 0
    l, r = len(left), len(right)
    while i < l and j < r:
        if left[i] <= right[j]:
            tmp.append(left[i])
            i += 1
        else:  # 此处使用else替换第二个if
            tmp.append(right[j])
            num += len(left) - i  # 对于每个right[j]，left中剩余的都是逆序对
            j += 1
    # 分别处理剩余元素
    tmp.extend(left[i:])
    tmp.extend(right[j:])

    return num, tmp


num ,tmp = merge_sort(arr)
print(num)