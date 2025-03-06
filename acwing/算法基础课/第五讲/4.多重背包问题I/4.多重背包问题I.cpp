#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

const int N = 110;

int f[N];

int main()
{
    int n, v;
    cin >> n >> v;
    for (int i = 1; i <= n; i++)
    {
        int vi, wi, si;
        cin >> vi >> wi >> si;
        for (int j = v; j >= 1; j--)
        {
            for (int k = 1; k <= si && j >= k * vi; k++)
            {
                f[j] = max(f[j], f[j - k * vi] + k * wi);
            }
        }
    }
    cout << f[v] << endl;
    return 0;
}