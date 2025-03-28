#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

const int N = 1000 + 10;

int f[N];

int main()
{
    int n, m;
    cin >> n >> m;
    while (n--)
    {
        int v, w, s;
        cin >> v >> w >> s;
        if (!s)
        {
            for (int j = v; j <= m; j++)
            {
                f[j] = max(f[j], f[j - v] + w);
            }
        }
        else
        {
            if (s == -1)
                s = 1;
            for (int k = 1; k <= s; k *= 2)
            {
                for (int j = m; j >= k * v; j--)
                    f[j] = max(f[j], f[j - k * v] + k * w);
                s -= k;
            }
            if (s)
            {
                for (int j = m; j >= s * v; j--)
                    f[j] = max(f[j], f[j - s * v] + s * w);
            }
        }
    }
    cout << f[m] << endl;
    return 0;
}