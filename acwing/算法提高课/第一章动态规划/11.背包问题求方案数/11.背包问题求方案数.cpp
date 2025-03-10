#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 1010, MOD = 1e9 + 7;

int f[N], g[N];

int main()
{
    int n, m;
    cin >> n >> m;
    for (int i = 0; i <= m; i++)
        g[i] = 1;
    for (int i = 1; i <= n; i++)
    {
        int v, w;
        cin >> v >> w;
        for (int j = m; j >= 0; j--)
        {
            if (j >= v)
            {
                if (f[j] < f[j - v] + w)
                {
                    f[j] = f[j - v] + w;
                    g[j] = g[j - v];
                }
                else if (f[j] == f[j - v] + w)
                {
                    g[j] = (g[j] + g[j - v]) % MOD;
                }
            }
        }
    }

    cout << g[m] << endl;
    return 0;
}