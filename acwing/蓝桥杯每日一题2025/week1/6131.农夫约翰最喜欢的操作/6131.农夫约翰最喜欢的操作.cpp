#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>

using namespace std;

const int N = 2 * 1e5 + 10;
typedef long long LL;

int w[N * 2];
LL s[2 * N];

int main()
{
    int t;
    scanf("%d", &t);
    while (t--)
    {
        int n, m;
        scanf("%d%d", &n, &m);
        for (int i = 1; i <= n; i++)
        {
            scanf("%d", &w[i]);
            w[i] %= m;
        }
        sort(w + 1, w + 1 + n);
        for (int i = 1; i <= n; i++)
            w[i + n] = w[i] + m;
        for (int i = 1; i <= 2 * n; i++)
            s[i] = s[i - 1] + w[i];
        LL res = 1e18;
        for (int i = 1; i <= n; i++)
        {
            int l = i, r = l + n - 1;
            int p = (l + r) / 2;
            LL left = (p - l + 1) * (LL)w[p] - (s[p] - s[l - 1]);
            LL right = s[r] - s[p] - (r - p) * (LL)w[p];
            res = min(res, left + right);
        }
        printf("%lld\n", res);
    }
    return 0;
}
