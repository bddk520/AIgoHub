#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

const int N = 15, M = 20;

int f[N][M];
int a[N][M];
int way[N];

int main()
{
    int n, m;
    cin >> n >> m;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            cin >> a[i][j];
        }
    }
    for (int i = 1; i <= n; i++)
    {
        for (int j = 0; j <= m; j++)
        {
            for (int k = 0; k <= j; k++)
            {
                f[i][j] = max(f[i][j], f[i - 1][j - k] + a[i][k]);
            }
        }
    }
    cout << f[n][m] << endl;
    int j = m;
    for (int i = n; i > 0; i--)
    {
        for (int k = 1; k <= j; k++)
        {
            if (f[i][j] == f[i - 1][j - k] + a[i][k])
            {
                way[i] = k;
                j -= k;
                break;
            }
        }
    }
    for (int i = 1; i <= n; i++)
        cout << i << " " << way[i] << endl;
    return 0;
}