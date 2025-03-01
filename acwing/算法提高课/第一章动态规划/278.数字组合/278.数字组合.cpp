#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 105, M = 10000 + 10;

int f[M];


int main()
{
    int n, m;
    cin >> n >> m;
    f[0] = 1;
    for (int i = 1; i <= n; i++)
    {
        int w;
        cin >> w;
        for (int j = m; j >= w; j--)
        {
            f[j] += f[j - w];
        }
    }
    printf("%d\n", f[m]);
    return 0;
}