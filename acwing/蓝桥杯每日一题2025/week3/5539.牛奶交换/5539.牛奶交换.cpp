#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>

using namespace std;

typedef long long LL;

const int N = 4 * 1e5 + 10;
char s[N];
int a[N];

int main()
{
    int n, m;
    scanf("%d%d", &n, &m);
    scanf("%s", s + 1);
    LL sum = 0;
    for (int i = 1; i <= n; i++)
    {
        scanf("%d", a + i);
        sum += a[i];
        a[i + n] = a[i];
    }
    int k = 1;
    while (k < n && s[k] == s[k + 1])
    {
        k++;
    }
    if (k < n)
    {
        for (int i = k + 1; i <= n + k; i++)
        {
            int j = i;
            LL res = 0;
            while (j <= n + k && s[j] == s[i])
            {
                res += a[j];
                j++;
                
            }
            if (s[i] == 'R')
                res -= a[j];
            else
                res -= a[i];

            sum -= min(res, (LL)m);
            i = j - 1;
        }
    }
    printf("%lld", sum);
    return 0;
}