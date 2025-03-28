#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <vector>

using namespace std;

typedef long long LL;

int mypow(int a, int b)
{
    int res = 1;
    for (int i = 1; i <= b; i++)
    {
        res *= a;
    }
    return res;
}

void solution(LL n, int k)
{
    LL temp_n = n;
    // vector<pair<int,int>> primes;
    for (int i = 2; i <= n / i; i++)
    {
        if (n % i == 0)
        {
            int s = 0;
            while (n % i == 0)
            {
                s += 1;
                n /= i;
            }
            if (s < k)
            {
                temp_n /= (mypow(i, s));
            }
        }
    }
    if (n > 1)
    {
        temp_n /= n;
    }
    cout << temp_n << endl;
}

int main()
{
    int q;
    cin >> q;
    for (int i = 0; i < q; i++)
    {
        LL n;
        int k;
        cin >> n >> k;
        solution(n, k);
    }
}