#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <cmath>

using namespace std;

const int N = 105;
const double eps = 1e-8;

double a[N][N];

int n;

int gauss()
{
    int c, r;
    for (c = 0, r = 0; c < n; c++)
    {
        int t = r;
        for (int i = r; i < n; i++)
        {
            if (fabs(a[i][c]) > fabs(a[t][c]))
                t = i;
        }
        if (fabs(a[t][c]) < eps)
            continue;

        for (int i = c; i <= n; i++)
            swap(a[r][i], a[t][i]);
        for (int i = n; i >= c; i--)
            a[r][i] /= a[r][c];
        for (int i = r + 1; i < n; i++)
        {
            if (fabs(a[i][c]) > eps)
            {
                for (int j = n; j >= c; j--)
                {
                    a[i][j] -= a[i][c] * a[r][j];
                }
            }
        }
        r++;
    }
    if (r < n)
    {
        for (int i = r; i < n; i++)
        {
            if (fabs(a[i][n]) > eps)
                return 2;
        }
        return 1;
    }

    for (int i = n - 1; i >= 0; i--)
    {
        for (int j = i + 1; j < n; j++)
        {
            a[i][n] -= a[j][n] * a[i][j];
        }
    }

    return 0;
}

int main()
{
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j <= n; j++)
        {
            cin >> a[i][j];
        }
    }
    int t = gauss();
    if (t == 1)
    {
        cout << "Infinite group solutions" << endl;
    }
    else if (t == 2)
    {
        cout << "No solution" << endl;
    }
    else
    {
        for (int i = 0; i < n; i++)
        {
            printf("%.2lf\n", a[i][n]);
        }
    }
    return 0;
}