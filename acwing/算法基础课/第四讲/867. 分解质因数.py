n = int(input())

def divide(n):
    i = 2
    for i in range(2,n //i + 1):
        if(n % i == 0):
            s = 0
            while(n % i == 0):
                n //= i
                s += 1
            print(f"{i} {s}")
    if n > 1:
        print(f"{n} {1}")
    print()

for i in range(n):
    num = int(input())
    divide(num)


                
