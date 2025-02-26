N = 1010

f = [0] * N

n = int(input())

arr = list(map(int, input().split()))

for i in range(n):
    f[i] = 1 # 重点，别记忘了，因为arr[i] 本身就是一个长度为 1 的上升子序列，如果前面的数字都比该数字大的话，没法上升，初始化为1
    for j in range(i):
        if arr[j] < arr[i]:
            f[i] = max(f[i], f[j] + 1)

print(max(f))
