#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <vector>

using namespace std;

const int N = 12, M = 1 << 10, K = 110;

typedef long long LL;

LL f[N][K][M];
int cnt[M];
vector<int> state;
vector<int> he[M];
int n, m;

bool check(int state)
{
    if ((state >> 1) & state)
    {
        return false;
    }
    return true;
}

int count(int state)
{
    int res = 0;
    for (int i = 0; i < n; i++)
        res += (state >> i) & 1;
    return res;
}

int main()
{
    scanf("%d%d", &n, &m);
    for (int i = 0; i < (1 << n); i++)
    {
        if (check(i))
        {

            state.push_back(i);
            cnt[i] = count(i);
        }
    }
    for (int i = 0; i < state.size(); i++)
    {
        for (int j = 0; j < state.size(); j++)
        {
            int a = state[i], b = state[j];
            if ((a & b) == 0 && check(a | b))
                he[i].push_back(j);
        }
    }
    f[0][0][0] = 1;
    for (int i = 1; i <= n + 1; i++)
    {
        for (int j = 0; j < m + 1; j++)
        {
            for (int a = 0; a < state.size(); a++)
            {
                for (int b : he[a])
                {
                    int c = cnt[state[a]];
                    if (j >= c)
                    {
                        f[i][j][state[a]] += f[i - 1][j - c][state[b]];
                    }
                }
            }
        }
    }
    printf("%lld", f[n + 1][m][0]);
    return 0;
}
