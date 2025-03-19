#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>

using namespace std;

typedef long long LL;

const int N = 2 * 1e5 + 5;
LL a[N];
int b[N];

int main()
{
    int n, m;
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n; i++)
        scanf("%d", &a[i]);
    for (int i = 1; i <= m; i++)
        scanf("%d", &b[i]);

    for (int i = 1; i <= m; i++)
    {
        int t = 0;
        for (int j = 1; j <= n; j++)
        {
            if (t < a[j])
            {
                int eat = min(a[j], (LL)b[i]) - t;
                a[j] += eat;
                t += eat;
                if (t == b[i])
                    break;
            }
        }
    }
    for (int i = 1; i <= n; i++)
        printf("%lld\n", a[i]);

    return 0;
}