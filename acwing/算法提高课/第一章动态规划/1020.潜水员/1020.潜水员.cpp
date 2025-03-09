#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

const int M = 25, N = 85;
int f[M][N];

int main()
{
    int m, n;
    cin >> m >> n;
    int k;
    cin >> k;
    memset(f, 0x3f, sizeof(f));
    f[0][0] = 0;
    while (k--)
    {
        int a, b, c;
        cin >> a >> b >> c;
        for (int i = m; i >= 0; i--)
        {
            for (int j = n; j >= 0; j--)
            {
                f[i][j] = min(f[i][j], f[max(0, i - a)][max(0, j - b)] + c);
            }
        }
    }
    cout << f[m][n] << endl;

    return 0;
}