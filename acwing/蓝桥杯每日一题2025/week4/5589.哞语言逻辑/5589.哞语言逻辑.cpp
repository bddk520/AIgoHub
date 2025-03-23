#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

const int N = 2 * 1e5 + 10;

int l[N], r[N], id[N], cnt, p[N], ones[N], zeros[N];

int main()
{
    int n, q;
    cin >> n >> q;
    char str[10];
    for (int i = 1; i <= n; i++)
    {
        cin >> str;
        if (!strcmp(str, "true") || !strcmp(str, "or"))
            p[i] = 1;
        if (i & 1)
        {
            if (i == 1 || p[i - 1])
            {
                cnt++;
                l[cnt] = i;
                r[cnt - 1] = i - 2;

                if (cnt >= 2)
                    ones[cnt - 1] = ones[cnt - 2] + !zeros[i - 2];
                zeros[i] = !p[i];
            }
            else
            {
                zeros[i] = zeros[i - 2] + !p[i];
            }
            id[i] = cnt;
        }
    }
    r[cnt] = n;
    ones[cnt] = ones[cnt - 1] + !zeros[n];

    while (q--)
    {
        int left, right;
        cin >> left >> right >> str;
        int res = !strcmp(str, "true");
        int lid = l[id[left]], rid = r[id[right]];
        int a = ones[id[left] - 1] + ones[cnt] - ones[id[right]];
        int b = zeros[rid] - zeros[right];
        if (lid != left)
            b += zeros[left - 2];
        if ((res == (a || !b && true)) || (res == (a || !b && false)))
            cout << "Y";
        else
            cout << "N";
    }

    return 0;
}