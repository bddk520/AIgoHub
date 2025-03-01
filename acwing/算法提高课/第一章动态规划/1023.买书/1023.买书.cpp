#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

const int N = 1010;

int f[N];
int a[] = {0, 10, 20, 50, 100};

int main()
{
    int n;
    cin >> n;
    f[0] = 1;
    for (int i = 1; i <= 4; i++)
    {
        for (int j = i; j <= n; j++)
        {
            if (j >= a[i])
                f[j] += f[j - a[i]];
        }
    }

    cout << f[n];
    return 0;
}