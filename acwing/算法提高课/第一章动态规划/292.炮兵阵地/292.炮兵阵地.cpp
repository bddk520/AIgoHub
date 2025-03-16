#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

const int N = 105, M = 1 << 10;

int f[2][M][M];
int cnt[M];
int g[N];

vector<int> state;

int n, m;

int count(int s)
{
    int res = 0;
    for (int i = 0; i < m; i++)
        if (s >> i & 1)
            res += 1;
    return res;
}

int main()
{
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            char c;
            cin >> c;
            if (c == 'H')
                g[i] += 1 << j;
        }
    }
    for (int i = 0; i < 1 << m; i++)
    {
        if (!((i & (i >> 1)) || (i & (i >> 2))))
        {
            state.push_back(i);
            cnt[i] = count(i);
        }
    }

    for (int i = 1; i <= n; i++)
    {
        for (int j = 0; j < state.size(); j++)
        {
            for (int k = 0; k < state.size(); k++)
            {
                int a = state[j], b = state[k];
                f[i & 1][j][k] = 0; // 养成好习惯，清零
                if ((g[i] & a) || (g[i - 1] & b))
                    continue;
                for (int z = 0; z < state.size(); z++)
                {
                    int c = state[z];
                    // if (g[i - 2] & c)
                    //     continue;
                    if ((a & b) || (a & c) || (b & c))
                        continue;
                    f[i & 1][j][k] = max(f[i & 1][j][k], f[(i - 1) & 1][k][z] + cnt[a]);
                }
            }
        }
    }
    int res = 0;
    for (int j = 0; j < state.size(); j++)
        for (int k = 0; k < state.size(); k++)
            res = max(res, f[n & 1][j][k]);
    printf("%d", res);

    return 0;
}