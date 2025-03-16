n, m = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

for i in range(len(b)):
    l = 0
    r = b[i]
    for j in range(len(a)):
        
        if r and l < a[j]:
        
            if a[j] < r:
                
                tmp = a[j] - l
                l = a[j]
                a[j] += tmp
                
            else:
                a[j] += r - l
                
                r = 0
                break

for i in a:
    print(i)
            
            