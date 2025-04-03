def quick_sort(l,r,data):
    if l >= r:
        return
    mid = data[(l+r)//2]
    i = l-1
    j = r+1
    while i < j:
        while 1:
            i += 1
            if data[i] >= mid:
                break
        while 1:
            j -= 1
            if data[j] <= mid:
                break
        if i < j:
            data[i],data[j] = data[j],data[i]
    quick_sort(l,j,data)
    quick_sort(j+1,r,data)
    
    
n = int(input())
data = [int(x)for x in input().split()]
quick_sort(0,n-1,data)
print(' '.join(list(map(str,data))))
# print(map(str,data))