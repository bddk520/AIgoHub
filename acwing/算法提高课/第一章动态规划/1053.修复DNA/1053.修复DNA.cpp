#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>

using namespace std;

const int N = 1010;
int tr[N][4], ne[N], dar[N], idx;
int q[N], hh = 0, tt = -1;
char s[N];
int f[N][N];

int get(char s)
{
    if (s == 'A')
        return 0;
    if (s == 'T')
        return 1;
    if (s == 'G')
        return 2;
    if (s == 'C')
        return 3;
}

void insert()
{
    int p = 0;
    for (int i = 0; s[i]; i++)
    {
        int t = get(s[i]);
        if (!tr[p][t])
            tr[p][t] = ++idx;
        p = tr[p][t];
    }
    dar[p] = 1;
}

void build()
{
    for (int i = 0; i < 4; i++)
    {
        if (tr[0][i]) // 注意这里
            q[++tt] = tr[0][i];
    }

    while (hh <= tt)
    {
        int t = q[hh++];
        for (int i = 0; i < 4; i++)
        {
            int p = tr[t][i];
            if (!p)
            {
                tr[t][i] = tr[ne[t]][i];
            }
            else
            {
                ne[p] = tr[ne[t]][i];
                q[++tt] = p;
                dar[p] |= dar[ne[p]];
            }
        }
    }
}

int main()
{
    int t = 1;
    int n;
    while (scanf("%d", &n), n)
    {
        memset(tr, 0, sizeof(tr));
        memset(ne, 0, sizeof(ne));
        memset(dar, 0, sizeof(dar));
        memset(f, 0x3f, sizeof(f));
        idx = 0, hh = 0, tt = -1;
        f[0][0] = 0;
        for (int i = 0; i < n; i++)
        {
            scanf("%s", s);
            insert();
        }
        build();

        scanf("%s", s + 1);
        int m = strlen(s + 1);
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j <= idx; j++)
            {
                for (int k = 0; k < 4; k++)
                {
                    int t = get(s[i + 1]) != k;
                    int p = tr[j][k];
                    if (!dar[p])
                        f[i + 1][p] = min(f[i + 1][p], f[i][j] + t);
                }
            }
        }

        int res = 0x3f3f3f3f;
        for (int i = 0; i <= idx; i++)
            res = min(res, f[m][i]);
        if (res == 0x3f3f3f3f)
            printf("Case %d: -1\n",t++);
        else
            printf("Case %d: %d\n", t++, res);
    }
}