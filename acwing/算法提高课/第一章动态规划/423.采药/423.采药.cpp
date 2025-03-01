#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

const int T = 1010, M = 105;

typedef pair<int, int> PII;

int f[M][T];
PII a[M];

int main()
{
    int t, m;
    cin >> t >> m;
    for (int i = 1; i <= m; i++)
        cin >> a[i].first >> a[i].second;

    for (int i = 1; i <= m; i++)
    {
        for (int j = 1; j <= t; j++)
        {
            f[i][j] = f[i - 1][j];
            if (j >= a[i].first)
            {
                f[i][j] = max(f[i][j], f[i - 1][j - a[i].first] + a[i].second);
            }
        }
    }
    printf("%d\n", f[m][t]);

    return 0;
}