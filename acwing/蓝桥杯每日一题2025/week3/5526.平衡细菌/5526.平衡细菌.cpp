#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>
#include <cmath>

using namespace std;

const int N = 2 * 1e5 + 10;
long long a[N], d[N], dd[N];

int main()
{

    int n;
    cin >> n;
    for (int i = 1; i <= n; i++)
        cin >> a[i];
    for (int i = 1; i <= n; i++)
        d[i] = a[i] - a[i - 1];
    for (int i = 1; i <= n; i++)
        dd[i] = d[i] - d[i - 1];
    long long res = 0;
    for (int i = 1; i <= n; i++)
        res += abs(dd[i]);
    printf("%d", res);
    return 0;
}