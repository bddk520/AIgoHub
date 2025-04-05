n = int(input().strip())

a = list(map(int,input().strip().split()))

cnt = 0
for i in range(n):
    while(a[i] % 2 == 0):
        a[i] //= 2
    if(a[i] == 1):
        cnt += 1

print(cnt)
