#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>

using namespace std;

const int N = 1e4 + 10, M = 1e6 + 10, S = 55;

char s[M];
int tr[N * S][26], q[N * S], idx, ne[N * S], cnt[N * S], hh = 0, tt = -1;

void insert()
{
    int p = 0;
    for (int i = 0; s[i]; i++)
    {
        int u = s[i] - 'a';
        if (!tr[p][u])
            tr[p][u] = ++idx;
        p = tr[p][u];
    }
    cnt[p] += 1;
}

void build()
{
    for (int i = 0; i < 26; i++)
    {
        if (tr[0][i])
            q[++tt] = tr[0][i];
    }

    while (hh <= tt)
    {
        int t = q[hh++];

        for (int i = 0; i < 26; i++)
        {
            int c = tr[t][i];
            if (!c)
            {
                tr[t][i] = tr[ne[t]][i];
            }
            else
            {
                ne[c] = tr[ne[t]][i];
                q[++tt] = c;
            }
        }
    }
}

int main()
{
    int t;
    scanf("%d", &t);
    while (t--)
    {
        memset(tr, 0, sizeof tr);
        memset(cnt, 0, sizeof cnt);
        memset(ne, 0, sizeof ne);
        idx = 0;
        hh = 0, tt = -1;
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
        {
            scanf("%s", s);
            insert();
        }
        build();

        scanf("%s", s);
        int res = 0;
        for (int i = 0, j = 0; s[i]; i++)
        {
            int u = s[i] - 'a';

            j = tr[j][u];
            int p = j;
            while (p && cnt[p] != -1)
            {
                res += cnt[p];
                cnt[p] = -1;
                p = ne[p];
            }
        }
        printf("%d", res);
    }
}