#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

const int N = 505;

int g[N][N];

int st[N], d[N];

int n, m;

void prim()
{
    int res = 0;
    memset(d, 0x3f, sizeof(d));
    d[1] = 0;
    for (int i = 0; i < n; i++)
    {
        int t = -1;
        for (int j = 1; j <= n; j++)
        {
            if (!st[j] && (t == -1 || d[t] > d[j]))
                t = j;
        }
        if (d[t] == 0x3f3f3f3f)
        {
            cout << "impossible" << endl;
            return;
        }
        res += d[t];
        st[t] = 1;
        for (int j = 1; j <= n; j++)
            d[j] = min(d[j], g[t][j]);
        
    }
    cout << res << endl;
}

int main()
{
    cin >> n >> m;
    memset(g, 0x3f, sizeof(g));
    for (int i = 0; i < m; i++)
    {
        int u, v, w;
        cin >> u >> v >> w;
        g[u][v] = g[v][u] = min(g[u][v], w);
    }
    prim();
    return 0;
}