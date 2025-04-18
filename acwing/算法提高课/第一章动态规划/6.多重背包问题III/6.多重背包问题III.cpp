#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

const int V = 20000 + 10;

int f[V], g[V], q[V];
int hh = 0, tt = -1;

int main()
{
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        int v, w, s;
        cin >> v >> w >> s;
        memcpy(g, f, sizeof(f));
        for (int j = 0; j < v; j++)
        {
            hh = 0, tt = -1;
            for (int k = j; k <= m; k += v)
            {
                if (hh <= tt && q[hh] < k - s * v)
                    hh++;
                while (hh <= tt && g[q[tt]] - (q[tt] - j) / v * w <= g[k] - (k - j) / v * w)
                {
                    tt--;
                }
                q[++tt] = k;
                f[k] = g[q[hh]] + (k - q[hh]) / v * w;
            }
        }
    }
    cout << f[m] << endl;
}