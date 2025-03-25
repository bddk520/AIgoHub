#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>

using namespace std;

static unsigned long _next = 1;
const int N = 2010, INF = 1e8;

double dt;

double v[N], u[N], a[N], b[N], c[N], d[N], I[1024][N / 2];
int r[N], cnt[N];

typedef pair<double, int> PDI;

int e[N], ne[N], h[N], idx;

PDI W[N];

/* RAND_MAX assumed to be 32767 */
int myrand(void)
{
    _next = _next * 1103515245 + 12345;
    return ((unsigned)(_next / 65536) % 32768);
}

void add(int a, int b, double w, int D)
{
    e[idx] = b;
    ne[idx] = h[a];
    W[idx] = {w, D};
    h[a] = idx++;
}

int main()
{
    int n, S, P, T;
    cin >> n >> S >> P >> T;
    cin >> dt;

    for (int i = 0; i < n;)
    {
        int rn = 0;
        cin >> rn;
        double vv, uu, aa, bb, cc, dd;
        cin >> vv >> uu >> aa >> bb >> cc >> dd;
        for (int j = 0; j < rn; j++, i++)
        {
            v[i] = vv, u[i] = uu, a[i] = aa, b[i] = bb, c[i] = cc, d[i] = dd;
        }
    }

    for (int i = 0; i < P; i++)
    {
        cin >> r[n + i];
    }
    memset(h, -1, sizeof(h));
    int mod = 0;
    for (int i = 0; i < S; i++)
    {
        int s, t, D;
        double w;
        cin >> s >> t >> w >> D;
        add(s, t, w, D);
        mod = max(mod, D + 1);
    }
    for (int i = 0; i < T; i++)
    {
        int ii = i % mod;
        for (int j = n; j < n + P; j++)
        {
            if (r[j] > myrand())
            {
                for (int k = h[j]; k != -1; k = ne[k])
                {
                    int t = e[k], D = W[k].second;
                    double w = W[k].first;
                    I[(ii + D) % mod][t] += w;
                }
            }
        }
        for (int j = 0; j < n; j++)
        {
            double vv = v[j], uu = u[j];
            v[j] = vv + dt * (0.04 * vv * vv + 5 * vv + 140 - uu) + I[ii][j];
            u[j] = uu + dt * a[j] * (b[j] * vv - uu);
            if (v[j] >= 30)
            {
                for (int k = h[j]; k != -1; k = ne[k])
                {
                    int t = e[k], D = W[k].second;
                    double w = W[k].first;
                    I[(ii + D) % mod][t] += w;
                }
                cnt[j]++;
                v[j] = c[j], u[j] += d[j];
            }
        }
        memset(I[ii], 0, sizeof I[ii]);
    }
    double max_v = -INF, min_v = INF;
    int max_cnt = -INF, min_cnt = INF;
    for (int i = 0; i < n; i++)
    {
        max_v = max(max_v, v[i]);
        min_v = min(min_v, v[i]);
        max_cnt = max(max_cnt, cnt[i]);
        min_cnt = min(min_cnt, cnt[i]);
    }
    printf("%.3lf %.3lf\n", min_v, max_v);
    printf("%d %d\n", min_cnt, max_cnt);
    return 0;
}