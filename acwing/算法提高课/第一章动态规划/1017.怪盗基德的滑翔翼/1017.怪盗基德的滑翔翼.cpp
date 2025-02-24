#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 55;
int f1[N];
int f2[N];
int h[N];

int main()
{
    int k;
    cin >> k;
    while (k--)
    {
        int n;
        cin >> n;
        for (int i = 1; i <= n; i++)
            cin >> h[i];
        for (int i = 1; i <= n; i++)
        {
            f1[i] = 1;
            f2[i] = 1;
            for (int j = 1; j < i; j++)
            {
                if (h[i] > h[j])
                {
                    f1[i] = max(f1[i], f1[j] + 1);
                }
                if (h[i] < h[j])
                {
                    f2[i] = max(f2[i], f2[j] + 1);
                }
            }
        }
        printf("%d\n", max(f1[n], f2[n]));
    }

    return 0;
}