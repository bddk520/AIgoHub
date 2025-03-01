#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

typedef long long LL;

const int N = 16, M = 3000 + 5;

LL f[M];

LL a[N];

int main()
{
    int n, m;
    cin >> n >> m;
    f[0] = 1;
    for (int i = 1; i <= n; i++)
    {
        int w;
        cin >> w;
        for (int j = 1; j <= m; j++)
        {
            if (j >= w)
                f[j] += f[j - w];
        }
    }
    cout << f[m];
    return 0;
}