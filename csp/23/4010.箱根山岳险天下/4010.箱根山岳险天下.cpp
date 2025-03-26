#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

typedef long long LL;

const int N = 3 * 1e5 + 10;

vector<int> q[N];
int thr;
int intense[N], cnt;

int main()
{
    int m, p, T;
    cin >> m >> p >> T;
    for (int i = 1; i <= m; i++)
    {
        int t;
        cin >> t;
        if (t == 1)
        {
            int x;
            cin >> x;
            if (T == 1)
            {
                x = x ^ thr;
            }
            if (x > 0)
            {
                q[i] = q[i - 1];
                q[i].push_back(++cnt);
                intense[cnt] = x;
            }
            else
            {
                q[i] = q[i - 1];
                q[i].pop_back();
            }
        }
        else if (t == 2)
        {
            int s, l, r, y;
            cin >> s >> l >> r >> y;
            q[i] = q[i - 1];
            if (T == 1)
            {
                y = y ^ thr;
            }
            for (int j = l - 1; j <= r - 1; j++)
            {
                LL ints = intense[q[s][j]];
                intense[q[s][j]] = (int)((ints * y) % p);
            }
        }
        else
        {
            int s, l, r;
            cin >> s >> l >> r;
            LL res = 0;
            q[i] = q[i - 1];
            for (int j = l - 1; j <= r - 1; j++)
            {
                res = (intense[q[s][j]] + res) % p;
            }
            cout << res << endl;
            thr = res;
        }
    }

    return 0;
}