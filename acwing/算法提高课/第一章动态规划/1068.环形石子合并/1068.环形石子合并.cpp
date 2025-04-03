#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>

using namespace std;

const int N = 405, INF = 0x3f3f3f3f;

int f[N][N], g[N][N];

int a[N], s[N];

int main()
{
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        cin >> a[i];
        a[i + n] = a[i];
    }
    for (int i = 1; i <= 2 * n; i++)
    {
        s[i] = s[i - 1] + a[i];
    }
    memset(f,0x3f,sizeof(f));
    memset(g,-0x3f,sizeof(g));
    for (int len = 1; len <= n; len++)
    {
        for (int i = 1; i + len - 1 <= 2 * n - 1; i++)
        {
            int j = i + len - 1;
            if (len == 1)
            {
                f[i][j] = 0;
                g[i][j] = 0;
            }
            else
            {
                for (int k = i; k <= j - 1; k++)
                {
                    f[i][j] = min(f[i][j], f[i][k] + f[k + 1][j] + s[j] - s[i - 1]);
                    g[i][j] = max(g[i][j], g[i][k] + g[k + 1][j] + s[j] - s[i - 1]);
                }
            }
        }
    }
    int max_v = -INF, min_v = INF;
    for (int i = 1; i <= n; i++)
    {
        min_v = min(min_v, f[i][n + i - 1]);
        max_v = max(max_v, g[i][i + n - 1]);
    }
    cout << min_v << endl
         << max_v << endl;
    return 0;
}