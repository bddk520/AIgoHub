#include <algorithm>
#include <cstring>
#include <cstdio>
#include <iostream>
#include <queue>

using namespace std;

const int N = 55;

typedef pair<int, int> PII;

int g[N][N], st[N][N];

int d[][2] = {{0, -1}, {-1, 0}, {0, 1}, {1, 0}};

int m, n;

int bfs(int x, int y)
{
    queue<PII> q; // 创建一个存储整型元素的队列
    q.push({x, y});
    st[x][y] = 1;
    int res = 1;
    while (!q.empty())
    {
        PII t = q.front();
        q.pop();
        int cur_x = t.first, cur_y = t.second;
        for (int i = 0; i < 4; i++)
        {
            if (g[cur_x][cur_y] >> i & 1)
                continue;
            int new_x = cur_x + d[i][0];
            int new_y = cur_y + d[i][1];
            if (new_x >= 0 && new_x < m && new_y >= 0 && new_y < n && !st[new_x][new_y])
            {

                q.push({new_x, new_y});
                res++;
                st[new_x][new_y] = 1;
            }
        }
    }
    return res;
}

int main()
{
    cin >> m >> n;
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> g[i][j];
        }
    }
    int cnt = 0;
    int max_res = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (!st[i][j])
            {
                cnt += 1;
                max_res = max(max_res, bfs(i, j));
            }
        }
    }
    cout << cnt << endl;
    cout << max_res << endl;
    return 0;
}