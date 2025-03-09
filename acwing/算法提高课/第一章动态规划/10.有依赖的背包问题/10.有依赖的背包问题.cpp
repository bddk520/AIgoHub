#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

const int N = 110;

int f[N][N];
int e[N], ne[N], h[N], idx;
int v[N], w[N];
int root;
int n, m;

void add(int a, int b)
{
    e[idx] = b;
    ne[idx] = h[a];
    h[a] = idx++;
}

void dfs(int u)
{
    for (int i = v[u]; i <= m; i++)
    {
        f[u][i] = w[u];
    }

    for (int i = h[u]; i != -1; i = ne[i])
    {
        int son = e[i];
        dfs(son);

        for (int j = m; j >= v[u]; j--)
        {
            for (int k = 0; k <= j - v[u]; k++)
            {
                f[u][j] = max(f[u][j], f[u][j - k] + f[son][k]);
            }
        }
    }
}

int main()
{
    memset(h, -1, sizeof(h));
    cin >> n >> m;
    for (int i = 1; i <= n; i++)
    {
        int p;
        cin >> v[i] >> w[i] >> p;
        if (p == -1)
        {
            root = i;
        }
        else
        {
            add(p, i);
        }
    }
    dfs(root);

    cout << f[root][m] << endl;
    return 0;
}