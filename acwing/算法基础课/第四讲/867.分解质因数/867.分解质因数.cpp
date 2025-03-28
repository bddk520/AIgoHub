#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

void prime(int n)
{
    for (int i = 2; i * i <= n; i++)
    {
        if (n % i == 0)
        {
            int s = 0;
            while (n % i == 0)
            {
                s += 1;
                n /= i;
            }
            cout << i << ' ' << s << endl;
        }
    }
    if (n > 1)
    {
        cout << n << ' ' << 1 << endl;
    }
    cout << endl;
}

int main()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int a;
        cin >> a;
        prime(a);
    }
    return 0;
}
