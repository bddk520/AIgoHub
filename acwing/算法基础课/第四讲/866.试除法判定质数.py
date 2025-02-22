import math

n = int(input())

def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

for i in range(n):
    num = int(input())
    if is_prime(num) == False:
        print("Yes")
    else:
        print("No")
        
        
