#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 1e6 + 10;

int a[N];
int q[N];
int tt = -1, hh = 0;

int main()
{
    int n, k;
    cin >> n >> k;
    for (int i = 1; i <= n; i++)
        cin >> a[i];
    for (int i = 1; i <= n; i++)
    {
        if (hh <= tt && q[hh] < i - k + 1)
            hh++;
        while (hh <= tt && a[q[tt]] >= a[i])
        {
            tt--;
        }
        q[++tt] = i;
        if (i > k - 1)
            cout << a[q[hh]] << " ";
    }
    cout << endl;
    hh = 0, tt = -1;
    for (int i = 1; i <= n; i++)
    {
        if (hh <= tt && q[hh] < i - k + 1)
            hh++;
        while (hh <= tt && a[q[tt]] <= a[i])
        {
            tt--;
        }
        q[++tt] = i;
        if (i > k - 1)
            cout << a[q[hh]] << " ";
    }
    cout << endl;

    return 0;
}