#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>

using namespace std;

const int N = 1010;

char g[N][N];
int st[N][N];

int d[][2] = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};

int n, m;

void dfs(int x, int y)
{
    if (st[x][y])
        return;
    st[x][y] = 1;
    for (int i = 0; i < 8; i++)
    {
        int new_x = d[i][0] + x;
        int new_y = d[i][1] + y;

        if (new_x >= 0 && new_x < n && new_y >= 0 && new_y < m && g[new_x][new_y] == 'W')
        {

            dfs(new_x, new_y);
        }
    }
}

int main()
{
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> g[i][j];
        }
    }

    int res = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (g[i][j] == 'W' && !st[i][j])
            {

                res++;
                dfs(i, j);
            }
        }
    }
    cout << res;
    return 0;
}