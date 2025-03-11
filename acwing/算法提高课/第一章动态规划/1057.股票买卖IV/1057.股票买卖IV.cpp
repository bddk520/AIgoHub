#include <algorithm>
#include <cstring>
#include <iostream>

using namespace std;

const int N = 1e5 + 10, K = 110;

int f[K][2];
int a[N];

int main()
{
    int n, k;
    cin >> n >> k;
    for (int i = 1; i <= n; i++)
        cin >> a[i];
    memset(f, -0x3f, sizeof(f));
    f[0][0] = 0;
    for (int i = 1; i <= n; i++)
    {
        for (int j = k; j >= 1; j--)
        {
            f[j][0] = max(f[j][0], f[j][1] + a[i]);
            f[j][1] = max(f[j][1], f[j - 1][0] - a[i]);
        }
    }
    int res = 0;
    for (int i = 0; i <= k; i++)
        res = max(res, f[i][0]);
    cout << res << endl;
    return 0;
}