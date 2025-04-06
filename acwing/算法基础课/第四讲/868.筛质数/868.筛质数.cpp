#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 1e6 + 10;

int primes[N], cnt, st[N];

int main()
{
    int n;
    cin >> n;
    for (int i = 2; i <= n; i++)
    {
        if (!st[i])
        {
            st[i] = 1;
            primes[cnt++] = i;
        }
        for (int j = 0; primes[j] <= n / i; j++)
        {
            st[primes[j] * i] = 1;
            if (i % primes[j] == 0)
                break;
        }
    }
    cout << cnt << endl;
    return 0;
}