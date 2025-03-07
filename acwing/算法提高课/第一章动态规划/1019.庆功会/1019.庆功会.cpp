#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

const int N = 6000 + 10;

int f[N];

int main()
{
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        int v, w, s;
        cin >> v >> w >> s;
        for (int j = m; j > 0; j--)
        {
            for (int k = 1; k <= s && j >= k * v; k++)
            {
                f[j] = max(f[j], f[j - k * v] + k * w);
            }
        }
    }
    cout << f[m] << endl;
    return 0;
}