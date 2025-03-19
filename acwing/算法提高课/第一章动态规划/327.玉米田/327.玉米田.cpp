#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

const int N = 14, M = 1 << 10, MOD = 1e8;

int f[N][M], st[N][N];

vector<int> state[N];
vector<int> he[N][M];

int m, n;

bool check(int m, int a)
{
    for (int i = 0; i < n; i++)
    {
        if ((st[m][i + 1] >= (a >> i & 1)) && (a >> 1 & a) == 0)
            continue;
        else
            return false;
    }
    return true;
}

int main()
{
    scanf("%d%d", &m, &n);

    for (int i = 1; i <= m; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            scanf("%d", &st[i][j]);
        }
    }
    for (int i = 1; i <= m; i++)
    {
        for (int j = 0; j < 1 << n; j++)
        {
            if (check(i, j))
            {
                state[i].push_back(j);
            }
        }
    }
    for (int i = 2; i <= m; i++)
    {
        for (int j = 0; j < state[i].size(); j++)
        {
            for (int z = 0; z < state[i - 1].size(); z++)
            {
                if ((state[i][j] & state[i - 1][z]) == 0)
                {
                    he[i][state[i][j]].push_back(state[i - 1][z]);
                }
            }
        }
    }
    f[0][0] = 1;
    for (int i = 1; i <= m + 1; i++)
    {
        for (int j : state[i])
        {
            if (i == 1)
            {
                f[i][j] += 1;
            }
            else
            {
                for (int z : he[i][j])
                {
                    f[i][j] = (f[i - 1][z] + f[i][j]) % MOD;
                }
            }
        }
    }
    int res = 0;
    for (int i = 0; i < 1 << n; i++)
    {

        res = (res + f[m][i]) % MOD;
    }
    printf("%d", res);
    return 0;
}