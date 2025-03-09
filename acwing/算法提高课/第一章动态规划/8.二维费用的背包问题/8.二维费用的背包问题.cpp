#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

const int V = 110, M = 110;
int f[V][M];

int main()
{
    int n, v, m;
    cin >> n >> v >> m;
    while (n--)
    {

        int vi, mi, wi;
        cin >> vi >> mi >> wi;
        for (int j = v; j >= vi; j--)
        {
            for (int k = m; k >= mi; k--)
            {
                f[j][k] = max(f[j][k], f[j - vi][k - mi] + wi);
            }
        }
    }
    cout << f[v][m] << endl;
    return 0;
}