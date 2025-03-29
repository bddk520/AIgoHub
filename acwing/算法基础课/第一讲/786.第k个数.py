'''
Author: bddk
Date: 2024-02-12 12:00:35
LastEditors: bddk
LastEditTime: 2024-02-12 13:54:56
'''

n, k = map(int, input().split())
arr = list(map(int, input().split()))


def quick_sort(arr, l, r, k):
    if l == r:
        return arr[l]
    i = l - 1
    j = r + 1
    x = arr[(r + l) // 2]
    while i < j:
        while True:
            i += 1
            if arr[i] >= x:
                break
        while True:
            j -= 1
            if arr[j] <= x:
                break
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if j - l + 1 >= k:
        return quick_sort(arr, l, j, k)
    else:
        return quick_sort(arr, j+1, r, k-(j - l+1))


print(quick_sort(arr, 0, len(arr)-1, k))
