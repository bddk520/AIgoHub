#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 2 * 1e5 + 10;

int c[N];

int main()
{
    int n, q;
    cin >> n >> q;

    for (int i = 0; i < n; i++)
    {
        cin >> c[i];
    }

    for (int i = 0; i < n; i++)
    {
        int t;
        cin >> t;

        c[i] = c[i] - t;
    }

    sort(c, c + n);

    while (q--)
    {
        int v, s;
        cin >> v >> s;
        int l = 0, r = n - 1;

        while (l < r)
        {
            int mid = (l + r) / 2;
            if (c[mid] > s)
                r = mid;
            else
                l = mid + 1;
        }

        if (c[l] > s && n - l >= v)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }

    return 0;
}