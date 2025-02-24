#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 11;

int f[2 * N][N][N];
int w[N][N];

int main()
{
    int n;
    cin >> n;
    int a, b, c;
    while (cin >> a >> b >> c, a || b || c)
    {
        w[a][b] = c;
    }
    for (int k = 2; k <= 2 * n; k++)
    {
        for (int i1 = 1; i1 <= n; i1++)
        {
            for (int i2 = 1; i2 <= n; i2++)
            {
                int j1 = k - i1, j2 = k - i2;
                if (j1 >= 1 && j1 <= n && j2 >= 1 && j2 <= n)
                {
                    int t = w[i1][j1];
                    if (i1 != i2)
                        t += w[i2][j2];
                    f[k][i1][i2] = max(f[k][i1][i2], f[k - 1][i1 - 1][i2 - 1] + t);
                    f[k][i1][i2] = max(f[k][i1][i2], f[k - 1][i1 - 1][i2] + t);
                    f[k][i1][i2] = max(f[k][i1][i2], f[k - 1][i1][i2 - 1] + t);
                    f[k][i1][i2] = max(f[k][i1][i2], f[k - 1][i1][i2] + t);
                }
            }
        }
    }
    printf("%d\n", f[2 * n][n][n]);
    return 0;
}