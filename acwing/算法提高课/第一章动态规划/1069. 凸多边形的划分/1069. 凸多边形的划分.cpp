#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>

using namespace std;

const int N = 105;

int a[N], f[N][N];

int main()
{
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        cin >> a[i];
        a[i + n] = a[i];
    }

    memset(f,0x3f,sizeof(f));

    for(int i = 1;i <= 2 * n;i++)

    return 0;
}