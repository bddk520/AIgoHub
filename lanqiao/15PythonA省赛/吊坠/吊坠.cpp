#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>

using namespace std;

const int N = 205, M = 55;

int g[N][N], st[N], d[N];

string a[N];

int cal(string a, string b)
{
    int cnt = 0;
    int f[2 * M][2 * M];
    memset(f, 0, sizeof(f));

    // 从1开始，避免访问负索引
    for (int i = 1; i <= a.size(); i++)
    {
        for (int j = 1; j <= b.size(); j++)
        {
            if (a[i - 1] == b[j - 1]) // 对应字符相同，调整索引进行比较
            {
                f[i][j] = f[i - 1][j - 1] + 1;
                cnt = max(f[i][j], cnt);
            }
        }
    }
    return cnt;
}

int main()
{
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
        a[i] += a[i];
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = i; j < n; j++)
        {
            g[i][j] = g[j][i] = min(m, cal(a[i], a[j]));
        }
    }
    // for (int i = 0; i < n; i++)
    // {
    //     for (int j = 0; j < n; j++)
    //     {
    //         cout << g[i][j] << ' ';
    //     }
    //     cout << endl;
    // }
    int res = 0;

    for (int i = 0; i < n; i++)
    {
        int t = -1;
        for (int j = 0; j < n; j++)
        {
            if (!st[j] && (t == -1 || d[t] < d[j]))
            {
                t = j;
            }
        }
        st[t] = 1;
        res += d[t];
        for (int j = 0; j < n; j++)
        {
            d[j] = max(d[j], g[t][j]);
        }
    }
    cout << res << endl;
    return 0;
}