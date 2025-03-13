#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

const int N = 55, MOD = 1e9 + 7;
int f[N][N], ne[N], ne_map[N][26];
char s[N];

int main()
{
    int n;
    cin >> n >> (s + 1);
    int m = strlen(s + 1);
    f[0][0] = 1;
    for (int i = 2, j = 0; i <= m; i++)
    {
        while (j && s[i] != s[j + 1])
        {
            j = ne[j];
        }
        if (s[i] == s[j + 1])
        {
            j++;
        }
        ne[i] = j;
    }

    for (int j = 0; j < m; j++)
    {
        for (int k = 0; k < 26; k++)
        {
            int u = j;
            while (u && 'a' + k != s[u + 1])
                u = ne[u];
            if ('a' + k == s[u + 1])
                u++;
            ne_map[j][k] = u;
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            for (int k = 0; k < 26; k++)
            {
                int u = ne_map[j][k];
                if (u < m)
                    f[i + 1][u] = (f[i + 1][u] +  f[i][j]) % MOD;
            }
        }
    }
    int res = 0;
    for (int i = 0; i < m; i++)
        res = (res + f[n][i]) % MOD;

    cout << res << endl;
}