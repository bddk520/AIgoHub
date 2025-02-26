#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 100000 + 10;

int f[N], a[N];

int main()
{
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++)
        cin >> a[i];

    int len = 0;
    for (int i = 1; i <= n; i++)
    {
        int l = 0;
        int r = len;

        while (l < r)
        {
            int mid = (l + r + 1) >> 1;
            if (f[mid] < a[i])
            {
                l = mid;
            }
            else
            {
                r = mid - 1;
            }
        }
        len = max(len, r + 1);
        f[r + 1] = a[i];
    }
    printf("%d\n", len);
    return 0;
}