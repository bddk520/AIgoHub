#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>

using namespace std;

int main()
{
    int n;
    scanf("%d", &n);
    int res = 0;
    while (n--)
    {
        int x;
        scanf("%d", &x);
        res ^= x;
    }
    if (res)
        printf("Yes");
    else
        printf("No");
    return 0;
}