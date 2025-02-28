
// 记录全局最小值的做法
// #include <iostream>
// #include <algorithm>
// #include <cstring>

// using namespace std;

// const int N = 55;

// int f[N], g[N], a[N];

// int ans;

// int n;

// void dfs(int u, int su, int sd)
// {
//     if (su + sd >= ans)
//         return;
//     if (u == n)
//     {
//         ans = min(ans, su + sd);
//         return;
//     }

//     int k = 0;
//     while (k < su && f[k] >= a[u])
//         k++;
//     if (k < su)
//     {
//         int t = f[k];
//         f[k] = a[u];
//         dfs(u + 1, su, sd);
//         f[k] = t;
//     }
//     else
//     {
//         f[k] = a[u];
//         dfs(u + 1, su + 1, sd);
//     }

//     k = 0;
//     while (k < sd && g[k] <= a[u])
//     {
//         k++;
//     }
//     if (k < sd)
//     {
//         int t = g[k];
//         g[k] = a[u];
//         dfs(u + 1, su, sd);
//         g[k] = t;
//     }
//     else
//     {
//         g[k] = a[u];
//         dfs(u + 1, su, sd + 1);
//     }
// }

// int main()
// {

//     while (cin >> n, n)
//     {
//         memset(f, 0, sizeof(f));
//         memset(g, 0, sizeof(g));
//         for (int i = 0; i < n; i++)
//             cin >> a[i];
//         ans = n;
//         dfs(0, 0, 0);
//         printf("%d\n", ans);
//     }

//     return 0;
// }

// 迭代加深的做法

#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

const int N = 55;

int f[N], g[N], a[N];

int n;

bool dfs(int depth, int u, int su, int sd)
{
    if (su + sd > depth)
        return false;
    if (u == n)
    {
        return true;
    }

    int k = 0;
    while (k < su && f[k] >= a[u])
        k++;
    if (k < su)
    {
        int t = f[k];
        f[k] = a[u];
        if (dfs(depth, u + 1, su, sd))
            return true;
        f[k] = t;
    }
    else
    {
        f[k] = a[u];
        if (dfs(depth, u + 1, su + 1, sd))
            return true;
    }

    k = 0;
    while (k < sd && g[k] <= a[u])
    {
        k++;
    }
    if (k < sd)
    {
        int t = g[k];
        g[k] = a[u];
        if (dfs(depth, u + 1, su, sd))
            return true;
        g[k] = t;
    }
    else
    {
        g[k] = a[u];
        if (dfs(depth, u + 1, su, sd + 1))
            return true;
    }
    return false; //注意别忘了
}

int main()
{

    while (cin >> n, n)
    {
        memset(f, 0, sizeof(f));
        memset(g, 0, sizeof(g));
        for (int i = 0; i < n; i++)
            cin >> a[i];
        int depth = 0;
        while (!dfs(depth, 0, 0, 0))
        {
            depth++;
        }
        printf("%d\n", depth);
    }

    return 0;
}