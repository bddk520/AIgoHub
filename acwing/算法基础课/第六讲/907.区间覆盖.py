# 暴力写法
# N = int(1e5) + 10

# arr = []

# s, t = map(int, input().split())

# n = int(input())

# for _ in range(n):
#     arr.append(list(map(int, input().split())))

# arr.sort(key=lambda x: x[0])
# res = 0
# while s <= t:
#     max_r = -2e9
#     for j in range(n):
#         if arr[j][0] <= s:
#             max_r = max(max_r, arr[j][1])
#         else:
#             break

#     if max_r == -2e9:
#         res = - 1
#         break
#     res += 1
#     s = max_r


# print(res)

arr = []

s, t = map(int, input().split())

n = int(input())

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: x[0])

res = 0
suscess = False
i  =  0
while i < n:
    j = i
    r = -2e9

    while j < n and arr[j][0] <= s:
        r = max(r,arr[j][1])
        j += 1
    
    if r < s:
        res = -1
        break

    res += 1
    if r >= t:
        suscess = True
        break 

    s = r
    i = j

print(res if suscess else -1)