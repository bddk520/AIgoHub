#include <algorithm>
#include <cstring>
#include <iostream>
#include <cstdio>

using namespace std;

const int N = 105, M = 10000 + 5;

int f[M];

class stone
{
public:
    int s, e, l;

public:
    bool operator<(const stone &other) const
    {
        return this->s * other.l < this->l * other.s;
    }
};

int main()
{
    int t;
    cin >> t;
    for (int k = 1; k <= t; k++)
    {
        memset(f, -0x3f, sizeof(f));
        f[0] = 0;
        stone a[N];
        int n;
        cin >> n;
        int m = 0;
        for (int j = 0; j < n; j++)
        {
            cin >> a[j].s >> a[j].e >> a[j].l;
            m += a[j].s;
        }
        sort(a, a + n);
        for (int i = 0; i < n; i++)
        {
            int s = a[i].s, e = a[i].e, l = a[i].l;
            for (int j = m; j >= s; j--)
            {
                f[j] = max(f[j], f[j - s] + e - (j - s) * l);
            }
        }
        int res = 0;
        for (int j = 0; j <= m; j++)
            res = max(res, f[j]);
        printf("Case #%d: %d\n", k, res);
    }
    return 0;
}
