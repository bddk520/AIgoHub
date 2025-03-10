#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

typedef pair<int, int> PII;

const int N = 60, M = 32010;
PII ms[N];
int f[M];
vector<PII> sv[N];

int main()
{
    int m, n;
    cin >> m >> n;
    for (int i = 1; i <= n; i++)
    {
        int v, p, q;
        cin >> v >> p >> q;
        if (q == 0)
        {
            ms[i] = {v, v * p};
        }
        else
        {
            sv[q].push_back({v, v * p});
        }
    }

    for (int i = 1; i <= n; i++)
    {
        if (ms[i].first == 0)
            continue;
        for (int u = m; u >= 0; u--)
        {
            for (int j = 0; j < 1 << sv[i].size(); j++)
            {
                int v = ms[i].first;
                int w = ms[i].second;
                for (int k = 0; k < sv[i].size(); k++)
                {
                    if (j >> k & 1)
                    {
                        v += sv[i][k].first;
                        w += sv[i][k].second;
                    }
                }
                if (u >= v)
                    f[u] = max(f[u], f[u - v] + w);
            }
        }
    }
    cout << f[m] << endl;
    return 0;
}
