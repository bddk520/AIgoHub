#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>

using namespace std;

const int N = 110;

int b[N];

int main()
{
    int n, max_sum = 0, min_sum = 0, cur;
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        cin >> b[i];
        if (i > 1)
        {
            max_sum += b[i];
            if (b[i] > cur)
            {
                min_sum += b[i];
                cur = b[i];
            }
            else
            {
                min_sum += 0;
            }
        }
        else
        {
            cur = b[i];
            max_sum += b[i];
            min_sum += b[i];
        }
    }
    cout << max_sum << endl
         << min_sum << endl;
    return 0;
}