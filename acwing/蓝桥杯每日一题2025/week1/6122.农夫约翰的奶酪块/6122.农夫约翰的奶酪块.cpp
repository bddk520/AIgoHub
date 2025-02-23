#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 1010;

int n, m;
int a[N][N];
int b[N][N];
int c[N][N];

int main()
{
    cin >> n >> m;
    int res = 0;
    while (m--)
    {
        int x, y, z;
        cin >> x >> y >> z;
        if (++a[x][y] == n)
        {
            res++;
        }
        if (++b[x][z] == n)
        {
            res++;
        }
        if (++c[z][y] == n)
        {
            res++;
        }
        printf("%d\n", res);
    }
}