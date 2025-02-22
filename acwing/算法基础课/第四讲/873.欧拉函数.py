n = int(input())

for _ in range(n):
    a = int(input())

    i = 2

    res = a
    while i * i <= a:

        if a % i == 0:
            # 注意这里，i会比1小很多，如果用//这里是0，则整个式子为res;或者写成 res = res / i  * (i - 1 ),因为res一定能整除i
            res = int(res * (1 - 1 / i))
            while a % i == 0:
                a //= i
        i += 1
    if a > 1:
        res = int(res * (1 - 1 / a))
    print(res)
