#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

const int N = 3 * 1e5 + 5;

vector<int> cnt;

char s[N];

int main()
{
    int n;
    scanf("%d", &n);

    scanf("%s", s);
    int r = n;
    for (int i = 0; s[i]; i++)
    {
        if (s[i] == '0')
            continue;
        int j = i + 1;
        while (j <= n && s[j] == '1')
        {
            j += 1;
        }
        int c = j - i;

        cnt.push_back(c);
        int d = (c - 1) / 2;
        if (!i || j == n)
            d = c - 1;
        r = min(r, d);
        i = j;
    }

    int res = 0;
    for (int i : cnt)
    {
        res += (i + 2 * r) / (2 * r + 1);
    }
    printf("%d", res);
    return 0;
}