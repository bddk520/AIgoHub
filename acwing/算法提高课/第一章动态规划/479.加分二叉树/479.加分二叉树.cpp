#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>

using namespace std;

const int N = 35;

int a[N], f[N][N], root[N][N];

void dfs(int l, int r)
{
    if (l > r)
        return;
    cout << root[l][r] << ' ';
    dfs(l, root[l][r] - 1);
    dfs(root[l][r] + 1, r);
}

int main()
{
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++)
        cin >> a[i];

    for (int i = 1; i <= n; i++)
    {
        f[i][i] = a[i];
        root[i][i] = i;
    }

    for (int len = 2; len <= n; len++)
    {
        for (int i = 1; i + len - 1 <= n; i++)
        {
            int j = i + len - 1;
            for (int k = i; k <= j; k++)
            {
                // if (k == i)
                // {
                //     f[i][j] = max(f[i][j], f[k + 1][j] + a[k]);
                // }
                // else if (k == j)
                // {
                //     f[i][j] = max(f[i][j], f[i][k - 1] + a[k]);
                // }
                // else
                // {
                //     f[i][j] = max(f[i][j], f[i][k - 1] * f[k + 1][j] + a[k]);
                // }
                int left = k == i ? 1 : f[i][k - 1];
                int right = k == j ? 1 : f[k + 1][j];
                int score = left * right + a[k];
                if (score > f[i][j])
                {
                    f[i][j] = score;
                    root[i][j] = k;
                }
            }
        }
    }
    cout << f[1][n] << endl;
    dfs(1, n);
    return 0;
}