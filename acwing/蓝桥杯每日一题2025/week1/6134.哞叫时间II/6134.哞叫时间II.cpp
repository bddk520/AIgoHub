#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>

using namespace std;

const int N = 1e6 + 10;
typedef long long LL;

int a[N], l[N], r[N], cnt;

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 1; i <= n; i++)
        scanf("%d", &a[i]);
    for (int i = 1; i <= n; i++)
    {
        int x = a[i];
        if (++l[x] == 1)
            cnt++;
    }
    LL res = 0;
    for (int i = n; i >= 1; i--)
    {
        int x = a[i];
        r[x] += 1;
        l[x] -= 1;
        if (l[x] == 0)
            cnt -= 1;
        if (r[x] == 2)
            res += cnt - (l[x] > 0 ? 1 : 0);
    }
    printf("%lld", res);
    return 0;
}