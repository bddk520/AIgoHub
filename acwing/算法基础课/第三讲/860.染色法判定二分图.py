from collections import deque

N = int(1e5) + 10
M = int(2e5) + 10

h = [-1] * N
e = [0] * M
ne = [0] * M
idx = 0
color = [0] * N
flag = 0


def add(a, b):
    global idx
    e[idx] = b
    ne[idx] = h[a]
    h[a] = idx
    idx += 1

# python的dfs会爆栈
# def dfs(u, c):
#     color[u] = c

#     i = h[u]

#     while i != -1:
#         j = e[i]

#         if color[j] == 0:
#             # color[j] = 3 -c
#             if  dfs(j, 3-c) == False:
#                 return False
#         else:
#             if color[j] == c:
#                 return False

#         i = ne[i]

#     return True

def bfs(u,c):
    q = deque()

    q.append(u)
    color[u] = c

    while q:
        t = q.popleft()

        i = h[t]

        while i != -1:
            j = e[i]

            if color[j] == 0:
                color[j] = 3 -color[t]
                q.append(j)
            else:
                if color[j] == color[t]:
                    return False

            i = ne[i]
    
    return True

n, m = map(int, input().split())

for _ in range(m):
    a, b = map(int, input().split())
    add(a, b)
    add(b, a)

flag = True

for i in range(1, n+1): # 有可能是非联通图,for循环遍历每个非联通图
    if color[i] == 0:
        flag = bfs(i,1)
        if flag == False:
            break
    

if flag:
    print("Yes")
else:
    print("No")             
