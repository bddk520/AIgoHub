# N = 12
# M = 1 << N

# f = [[0 for _ in range(M)] for _ in range(N)]
# st = [1] * M


# while True:
#     n, m = map(int, input().split())
#     if n == 0 and m == 0:
#         break

#     for i in range(1 << n):
#         is_valid = 1
#         cnt = 0
#         for j in range(n):
#             if (i >> j) & 1:
#                 if cnt & 1:
#                     is_valid = 0
#                     break
#             else:
#                 cnt += 1
#         if cnt & 1:
#             is_valid = 0
#         st[i] = is_valid
#     f = [[0 for _ in range(M)] for _ in range(N)]
#     f[0][0] = 1
#     for i in range(1, m + 1):
#         for j in range(1 << n):
#             for k in range(1 << n):
#                 if (j & k) == 0 and st[j | k]:
#                     f[i][j] += f[i - 1][k]

#     print(f[m][0])
N = 12
M = 1 << N

f = [[0 for _ in range(M)] for _ in range(N)]
st = [1] * M


while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    for i in range(1 << n):
        is_valid = 1
        cnt = 0
        for j in range(n):
            if (i >> j) & 1:
                if cnt & 1:
                    is_valid = 0
                    break
                cnt = 0
            else:
                cnt += 1
        if cnt & 1:
            is_valid = 0
        st[i] = is_valid
    states = []
    for i in range(1 << n):
        state = []
        for j in range(1 << n):
            if (i & j) == 0 and st[i | j]:
                state.append(j)
        states.append(state)
    f = [[0 for _ in range(M)] for _ in range(N)]
    f[0][0] = 1
    for i in range(1, m + 1):
        for j in range(1 << n):
            for k in states[j]:
                f[i][j] += f[i - 1][k]

    print(f[m][0])
