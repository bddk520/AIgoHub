#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>

using namespace std;

const int N = 1010, M = 15;

int a[N][M];

int main()
{
    int n, m;
    cin >> n >> m;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            cin >> a[i][j];
        }
    }
    for (int i = 1; i <= n; i++)
    {
        int f = 0;
        for (int j = 1; j <= n; j++)
        {
            if (j == i)
                continue;
            int flag = 1;
            for (int k = 1; k <= m; k++)
            {
                if (a[i][k] >= a[j][k])
                {
                    flag = 0;
                    break;
                }
            }
            if (flag)
            {
                cout << j << endl;
                f = 1;
                break;
            }
        }
        if (!f)
            cout << 0 << endl;
    }
    return 0;
}