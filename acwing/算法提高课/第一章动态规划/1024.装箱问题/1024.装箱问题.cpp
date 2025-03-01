#include <algorithm>
#include <iostream>
#include <cstring>

using namespace std;

const int N = 35, V = 20000 + 10;

int f[N][V];
int a[N];

int main()
{
    int v, n;
    cin >> v >> n;
    for (int i = 1; i <= n; i++)
    {
        cin >> a[i];
        for (int j = 1; j <= v; j++)
        {
            f[i][j] = f[i - 1][j];
            if (j >= a[i])
            {
                f[i][j] = max(f[i][j], f[i - 1][j - a[i]] + a[i]);
            }
        }
    }
    cout << (v - f[n][v]) << endl;
    return 0;
}