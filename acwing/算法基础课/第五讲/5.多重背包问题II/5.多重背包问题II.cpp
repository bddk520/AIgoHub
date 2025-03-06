#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>

using namespace std;

const int N = 2010;

int f[N];

typedef pair<int, int> PII;

int main()
{
    int n, v;
    cin >> n >> v;
    for (int i = 1; i <= n; i++)
    {
        int vi, wi, si;
        cin >> vi >> wi >> si;
        vector<PII> goods;

        int k = 1;
        while (si >= k)
        {
            si -= k;
            goods.push_back(make_pair(vi * k, wi * k));
            k *= 2;
        }
        if (si > 0)
        {
            goods.push_back(make_pair(vi * si, wi * si));
        }
        for (auto good : goods)
        {
            for (int j = v; j >= good.first; j--)
            {
                f[j] = max(f[j], f[j - good.first] + good.second);
            }
        }
    }
    cout << f[v] << endl;
    return 0;
}