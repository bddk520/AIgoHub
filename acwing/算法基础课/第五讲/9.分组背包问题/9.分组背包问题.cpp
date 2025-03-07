#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

const int N = 105;

int f[N], v[N], w[N];
int main()
{
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        int s;
        cin >> s;
        for (int j = 1; j <= s; j++)
        {
            cin >> v[j] >> w[j];
        }
        for (int j = m; j >= 1; j--)
        {
            for (int k = 1; k <= s; k++)
            {
                if (v[k] <= j)
                    f[j] = max(f[j], f[j - v[k]] + w[k]);
            }
        }
    }
    cout << f[m] << endl;
    return 0;
}