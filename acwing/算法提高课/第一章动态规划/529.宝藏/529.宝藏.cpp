#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>

using namespace std;

const int N = 15, INF = 0x3f3f3f3f;

int g[N][N], f[1 << N][N], ne[1 << N];

int main()
{
    int n, m;
    cin >> n >> m;
    memset(g, 0x3f, sizeof(g));
    for (int i = 0; i < n; i++)
        g[i][i] = 0;
    for (int i = 0; i < m; i++)
    {
        int a, b, c;
        cin >> a >> b >> c;
        a--; // 转换为0-based
        b--; // 转换为0-based
        g[b][a] = g[a][b] = min(g[a][b], c);
    }

    for (int i = 0; i < (1 << n); i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (i >> j & 1)
            {
                for (int k = 0; k < n; k++)
                {
                    if (g[j][k] != INF)
                    {
                        ne[i] |= 1 << k;
                    }
                }
            }
        }
    }
    memset(f, 0x3f, sizeof(f));
    for (int i = 0; i < n; i++)
        f[1 << i][0] = 0;
    for (int i = 0; i < 1 << n; i++)
    {
        for (int j = (i - 1) & i; j; j = (j - 1) & i)
        {
            
            if ((ne[j] & i) == i) // 注意运算符
            {
                int cost = 0;
                int remain = j ^ i;
                for (int k = 0; k < n; k++)
                {
                    if (remain >> k & 1)
                    {
                        int t = INF;
                        for (int u = 0; u < n; u++)
                        {
                            if (j >> u & 1)
                            {
                                t = min(t, g[u][k]);
                            }
                        }
                        cost += t;
                    }
                }
                for (int k = 1; k < n; k++)
                {
                    f[i][k] = min(f[i][k], f[j][k - 1] + cost * k);
                }
            }
        }
    }

    int res = INF;
    for (int i = 0; i < n; i++)
        res = min(res, f[(1 << n) - 1][i]);
    cout << res;
    return 0;
}
