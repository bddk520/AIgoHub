#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

const int N = 30000 + 10;

int f[N], w[N], v[N];

int main()
{
    int n, m;
    cin >> n >> m;
    for (int i = 1; i <= m; i++)
    {
        int vi, pi;
        cin >> vi >> pi;
        v[i] = vi;
        w[i] = vi * pi;
    }

    for (int i = 1; i <= m; i++)
    {
        for (int j = n; j >= v[i]; j--)
        {
            f[j] = max(f[j], f[j - v[i]] + w[i]);
        }
    }
    cout << f[n] << endl;
    return 0;
}