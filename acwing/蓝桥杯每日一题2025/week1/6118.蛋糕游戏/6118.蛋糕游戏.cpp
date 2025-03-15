#include <algorithm>
#include <iostream>
#include <cstring>

using namespace std;

const int N = 5 * 1e5 + 10;

typedef long long LL;

LL s[N];

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        LL res = 1e15;
        int l = n / 2 + 1;
        for (int i = 1; i <= n; i++)
        {
            int x;
            cin >> x;
            s[i] = s[i - 1] + x;
            if (i >= l)
                res = min(res, s[i] - s[i - l]);
        }
        cout << res << ' ' << s[n] - res << endl;
    }

    return 0;
}