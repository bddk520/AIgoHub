#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <cmath>

using namespace std;

const int N = 2 * 1e5 + 10;
int h[N], a[N], rk[N];

int main()
{
    int T;
    scanf("%d", &T);
    while (T--)
    {
        int n;
        scanf("%d", &n);
        for (int i = 1; i <= n; i++)
            scanf("%d", &h[i]);
        for (int i = 1; i <= n; i++)
            scanf("%d", &a[i]);
        for (int i = 1; i <= n; i++)
        {
            int t;
            scanf("%d", &t);
            rk[t + 1] = i;
        }
        int l = 0, r = 1e9;
        for (int i = 1; i < n; i++)
        {
            int A = h[rk[i]] - h[rk[i + 1]];
            int B = a[rk[i + 1]] - a[rk[i]];

            if (B > 0)
            {
                r = min(r, (int)ceil((double)A / B) - 1); //注意这里不能用floor(A/B )当 A /B是整数是，这里只有ceil((double)A / B) - 1
            }
            else if (B < 0)
            {
                l = max(l, (int)floor((double)A / B) + 1);
            }
            else if (A <= 0)
            {
                r = -1;
                break;
            }
        }
        if (l > r)
            l = -1;
        printf("%d\n", l);
    }

    return 0;
}