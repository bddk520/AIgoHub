#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <vector>
#include <unordered_map>

using namespace std;

typedef long long LL;

const int MOD = 1e9 + 7, N = 1e5 + 10, INF = 0x3f3f3f3f;

int R[N], C[N];
LL fact[2 * N], sr[N], sc[N];

unordered_map<int, int> cntr, cntc;

LL qmi(LL a, LL b)
{
    LL res = 1;
    while (b)
    {
        if (b & 1)
            res = (res * a) % MOD;
        b >>= 1;
        a = (a * a) % MOD;
    }
    return res;
}

bool check(int sr, int sc, int tr, int tc)
{
    if (R[sr] > R[tr] || C[sc] > C[tc])
        return false;
    if (R[sr] == R[tr] && sr != tr)
        return false;
    if (C[sc] == C[tc] && sc != tc)
        return false;
    return true;
}

int main()
{
    int n, m, T;
    cin >> n >> m >> T;
    // r[0] = -INF,c[0] = -INF;
    vector<int> r, c;
    r.push_back(-INF), c.push_back(-INF);
    for (int i = 1; i <= n; i++)
    {
        cin >> R[i];
        r.push_back(R[i]);
        cntr[R[i]]++;
    }
    for (int i = 1; i <= m; i++)
    {
        // int ci;
        cin >> C[i];
        c.push_back(C[i]);
        cntc[C[i]]++;
    }

    sort(r.begin(), r.end());
    sort(c.begin(), c.end());

    r.erase(unique(r.begin(), r.end()), r.end());
    c.erase(unique(c.begin(), c.end()), c.end());

    fact[0] = 1;
    for (int i = 1; i <= n + m; i++)
    {
        fact[i] = fact[i - 1] * i % MOD;
        // infact[i] = qmi(fact[i], MOD - 2);
        // cout << fact[i] << ' ' << infact[i] << endl;
    }
    sr[0] = 1;
    for (int i = 1; i < r.size(); i++)
    {
        sr[i] = (sr[i - 1]) * cntr[r[i]] % MOD;
    }

    sc[0] = 1;
    for (int i = 1; i < c.size(); i++)
    {
        sc[i] = sc[i - 1] * cntc[c[i]] % MOD;
    }

    while (T--)
    {
        int s_r, s_c, t_r, t_c;
        cin >> s_r >> s_c >> t_r >> t_c;

        if (!check(s_r, s_c, t_r, t_c))
        {
            cout << 0 << endl;
            continue;
        }

        int x1 = lower_bound(r.begin(), r.end(), R[s_r]) - r.begin();
        int y1 = lower_bound(c.begin(), c.end(), C[s_c]) - c.begin();
        int x2 = lower_bound(r.begin(), r.end(), R[t_r]) - r.begin();
        int y2 = lower_bound(c.begin(), c.end(), C[t_c]) - c.begin();

        LL res = 1;
        int a = x2 - x1 + y2 - y1;
        int b = x2 - x1;
        res = (res * fact[a]) % MOD;
        // cout << res << endl;
        res = (res * qmi(fact[b], MOD - 2)) % MOD;
        // cout << res << endl;
        res = (res * qmi(fact[a - b], MOD - 2)) % MOD;
        // cout << res << endl;
        if (x1 + 1 <= x2 - 1)
            res = (res * (sr[x2 - 1] * qmi(sr[x1], MOD - 2) % MOD)) % MOD;
        // cout << res << endl;
        if (y1 + 1 <= y2 - 1)
            res = (res * (sc[y2 - 1] * qmi(sc[y1], MOD - 2) % MOD)) % MOD;

        cout << res << endl;
    }

    return 0;
}