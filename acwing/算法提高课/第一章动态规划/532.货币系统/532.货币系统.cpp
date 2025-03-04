#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

const int N = 25000 + 10;

int f[N], a[N];

int main()
{
    int t;
    cin >> t;
    while ((t--))
    {
        int n;
        cin >> n;
        memset(f, 0, sizeof(f));
        memset(a, 0, sizeof(f));
        for (int i = 1; i <= n; i++)
            cin >> a[i];
        sort(a + 1, a + n + 1);
        int m = a[n];
        f[0] = 1;
        int res = 0;
        for (int i = 1; i <= n; i++)
        {
            if (f[a[i]] == 0)
                res++;
            for (int j = a[i]; j <= m; j++)
            {
                f[j] = f[j] | f[j - a[i]];
            }
        }
        cout << res << endl;
    }
    return 0;
}
