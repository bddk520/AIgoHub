#include <iostream>
#include <algorithm>
#include <cstring>
#include <cmath>
using namespace std;

const int N = 15, m = 8, INF = 1e9;

int a[N][N];
int s[N][N];
double f[N][N][N][N][N];
double sum = 0;
int n;

int get_sum(int x1, int y1, int x2, int y2)
{
    return s[x2][y2] - s[x2][y1 - 1] - s[x1 - 1][y2] + s[x1 - 1][y1 - 1];
}

double get(int x1, int y1, int x2, int y2)
{
    return double(get_sum(x1, y1, x2, y2)) * get_sum(x1, y1, x2, y2) / n;
}

double dfs(int k, int x1, int y1, int x2, int y2)
{
    double &v = f[x1][y1][x2][y2][k];
    if (v >= 0)
        return v;
    if (k == 1)
    {
        return v = get(x1, y1, x2, y2);
    }
    v = INF;
    for (int i = x1; i < x2; i++)
    {
        f[x1][y1][x2][y2][k] = min(f[x1][y1][x2][y2][k], dfs(k - 1, x1, y1, i, y2) + get(i + 1, y1, x2, y2));
        f[x1][y1][x2][y2][k] = min(f[x1][y1][x2][y2][k], dfs(k - 1, i + 1, y1, x2, y2) + get(x1, y1, i, y2));
    }

    for (int i = y1; i < y2; i++)
    {
        f[x1][y1][x2][y2][k] = min(f[x1][y1][x2][y2][k], dfs(k - 1, x1, y1, x2, i) + get(x1, i + 1, x2, y2));
        f[x1][y1][x2][y2][k] = min(f[x1][y1][x2][y2][k], dfs(k - 1, x1, i + 1, x2, y2) + get(x1, y1, x2, i));
    }

    return f[x1][y1][x2][y2][k];
}

int main()
{
    memset(f, -1, sizeof(f));
    cin >> n;
    for (int i = 1; i <= m; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            cin >> a[i][j];
            sum += a[i][j];
        }
    }
    sum = sum / n;

    for (int i = 1; i <= m; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + a[i][j];
        }
    }
    printf("%.3lf\n", sqrt(dfs(n, 1, 1, 8, 8) - sum * sum));
    return 0;
}