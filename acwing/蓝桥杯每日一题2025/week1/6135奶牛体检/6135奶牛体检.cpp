#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>

using namespace std;

const int N = 7500 + 10;
int a[N], b[N], ans[N];

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 1; i <= n; i++)
        scanf("%d", &a[i]);
    for (int i = 1; i <= n; i++)
        scanf("%d", &b[i]);

    int sum = 0;

    for (int i = 1; i <= n; i++)
    {
        if (a[i] == b[i])
        {
            sum += 1;
        }
    }

    for (int i = 1; i <= n; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            int cnt = sum;
            for (int l = i, r = i + j; l >= 1 && r <= n; l--, r++)
            {
                if (a[l] == b[l])
                    cnt--;
                if (a[r] == b[r])
                    cnt--;
                if (a[l] == b[r])
                    cnt++;
                if (a[r] == b[l])
                    cnt++;
                ans[cnt]++;
            }
        }
    }
    for (int i = 0; i <= n; i++)
        printf("%d\n", ans[i]);
    return 0;
}
