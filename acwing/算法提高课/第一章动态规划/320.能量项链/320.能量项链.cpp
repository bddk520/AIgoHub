#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>

using namespace std;

const int N = 110;

int f[2 * N][2 * N];

int a[2 * N];

int main()
{
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        cin >> a[i];
        a[i + n] = a[i];
    }
    memset(f, 0xcf, sizeof(f));
    for (int i = 1; i <= 2 * n; i++)
        f[i][i] = 0;

    for (int len = 2; len <= n; len++)
    {
        for (int i = 1; i + len - 1 < 2 * n; i++)
        {
            int j = i + len - 1;

            for (int k = i; k < j; k++)
            {
                f[i][j] = max(f[i][j], f[i][k] + f[k + 1][j] + a[i] * a[k + 1] * a[j + 1]);
            }
        }
    }

    int res = 0;
    for (int i = 1; i <= n; i++)
    {
        res = max(res, f[i][i + n - 1]);
    }
    cout << res << endl;

    return 0;
}