# 多循环，初始化

N = 110

f1 = [0] * N
f2 = [0] * N
h = []

k = int(input())

for _ in range(k):
    f1 = [0] * N
    f2 = [0] * N
    n = int(input())
    h = list(map(int,input().split()))

    for i in range(n):
        f1[i] = 1
        f2[i] = 1
        for j in range(i):
            if h[i] > h[j]:
                f1[i] = max(f1[i],f1[j] + 1)
            if h[i] < h[j]:
                f2[i] = max(f2[i],f2[j] + 1)
            
    print(max(max(f1),max(f2)))