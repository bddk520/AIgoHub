#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

const int N = 1010, M = 510, K = 105;

int f[N][M];

int main()
{
    int n, m, k;
    cin >> n >> m >> k;
    for (int i = 1; i <= k; i++)
    {
        int v1, v2;
        cin >> v1 >> v2;
        for (int j = n; j >= v1; j--)
        {
            for (int z = m - 1; z >= v2; z--)
            {
                f[j][z] = max(f[j][z], f[j - v1][z - v2] + 1);
            }
        }
    }
    cout << f[n][m - 1] << " ";
    int z = m - 1;
    while (z > 0 && f[n][z - 1] == f[n][m - 1])
        z--;
    cout << m - z << endl;
    return 0;
}