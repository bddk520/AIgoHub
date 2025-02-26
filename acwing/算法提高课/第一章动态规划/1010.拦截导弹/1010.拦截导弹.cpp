#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 1010;

int f[N], a[N], g[N];

int main()
{

    int n = 0;
    while (cin >> a[++n])
        ;
    n--;
    int res = 0;
    for (int i = 1; i <= n; i++)
    {
        f[i] = 1;
        for (int j = 1; j < i; j++)
        {
            if (a[i] <= a[j])
                f[i] = max(f[i], f[j] + 1);
        }
        res = max(res, f[i]);
    }
    printf("%d\n", res);

    int cnt = 0;
    for (int i = 1; i <= n; i++)
    {
        int k = 0;
        while (k < cnt && g[k] < a[i])
        {
            k++;
        }
        g[k] = a[i];
        if (k >= cnt)
            cnt++;
    }
    printf("%d\n", cnt);

    return 0;
}