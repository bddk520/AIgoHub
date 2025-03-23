// 暴力

// #include <iostream>
// #include <cstring>
// #include <cstdio>
// #include <algorithm>

// using namespace std;

// const int N = 5 * 1e5 + 10;

// int a[N];

// int main()
// {
//     int n;
//     cin >> n;
//     for (int i = 1; i <= n; i++)
//         cin >> a[i];

//     int res = 0;
//     for (int p = 1; p <= 1e4; p++)
//     {
//         int cnt = 0;
//         for (int i = 1; i <= n; i++)
//         {
//             if (a[i] < p)
//                 continue;
//             int j = i;
//             cnt += 1;
//             while (j <= n && a[j + 1] >= p)
//             {
//                 j++;
//             }
//             i = j + 1;
//         }
//         res = max(res, cnt);
//     }
//     cout << res << endl;
//     return 0;
// }

#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>

using namespace std;

const int N = 5 * 1e5 + 10, M = 1e4 + 10;

int a[N], cnt[N];

int main()
{
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++)
        cin >> a[i];
    n = unique(a + 1, a + 1 + n) - a - 1;
    a[0] = 0, a[n + 1] = 0;
    for (int i = 1; i <= n; i++)
    {
        int x = a[i - 1], y = a[i], z = a[i + 1];
        if (x < y && y > z)
            cnt[y] += 1;
        else if (x > y && y < z)
            cnt[y] -= 1;
    }
    int res = 0;
    int sum = 0;
    for (int i = M; i; i--)
    {
        sum += cnt[i];
        res = max(res, sum);
    }
    cout << res << endl;
    return 0;
}