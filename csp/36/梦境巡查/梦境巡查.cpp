// #include <iostream>
// #include <algorithm>
// #include <cstring>
// #include <cstdio>

// using namespace std;

// const int N = 1e5 + 10, INF = 0x3f3f3f3f;

// int a[N], b[N], s[N];

// int main()
// {
//     int n;
//     cin >> n;
//     for (int i = 0; i <= n; i++)
//     {
//         cin >> a[i];
//     }
//     for (int i = 1; i <= n; i++)
//         cin >> b[i];
//     for (int i = 1; i <= n; i++)
//     {
//         int min_res = INF;
//         int res = 0;
//         for (int j = 0; j <= n; j++)
//         {
//             if (j != i)
//             {
//                 res += b[j] - a[j];
//             }
//             else
//             {
//                 res += -a[j];
//             }
//             min_res = min(min_res, res);
//         }
//         cout << -1 * min_res << ' ';
//     }
// }
#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>

using namespace std;

const int N = 1e5 + 10, INF = 0x3f3f3f3f;

int a[N], b[N], s[N], f[N], ba[N];

int main()
{
    int n;
    cin >> n;
    for (int i = 0; i <= n; i++)
    {
        cin >> a[i];
    }
    for (int i = 1; i <= n; i++)
        cin >> b[i];
    memset(ba, 0xcf, sizeof(ba));
    for (int i = 1; i <= n + 1; i++)
    {
        s[i] = s[i - 1] + a[i - 1] - b[i - 1];
        f[i] = max(f[i - 1], s[i]);
    }
    for (int i = n + 1; i >= 1; i--)
    {
        ba[i] = max(ba[i + 1], s[i]);
        // cout << ba[i] << endl;
    }
    for (int i = 1; i <= n; i++)
    {
        cout << max(f[i], b[i] + ba[i + 1]) << ' ';
    }
}