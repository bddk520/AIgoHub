#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <vector>

using namespace std;

const int N = 16, M = 1 << 16;

vector<int> states[N];
double p[N];
double f[M][N * 5 + 1];

int n, k;

double dp(int state, int coins, int r)
{
    double &v = f[state][coins];
    if (v >= 0)
        return v;
    if (coins >= r * k)
        return v = 0;

    v = 0;
    for (int i = 0; i < n; i++)
    {
        if (state >> i & 1)
        {
            v += p[i] * (dp(state, coins + 1, r) + 1);
        }
        else
        {
            v += p[i] * (dp(state | (1 << i), coins, r - 1) + 1);
        }
    }
    return v;
}

int main()
{
    cin >> n >> k;
    for (int i = 0; i < n; i++)
        cin >> p[i];
    memset(f, -1, sizeof(f));
    printf("%.10lf\n", dp(0, 0, n));
}