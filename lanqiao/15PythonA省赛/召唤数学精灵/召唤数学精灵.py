def SUM(i):
    return (i * (i + 1)) // 2




n = 2024041331404202

cnt = 0
mul_res = 362880
for i in range(10,200 + 1):
    mul_res *= i;
    if (SUM(i) - mul_res) % 100 == 0:
        print(i)
        cnt += 1
print(cnt)

print(2024041331404202 // 200 * cnt + 2)
