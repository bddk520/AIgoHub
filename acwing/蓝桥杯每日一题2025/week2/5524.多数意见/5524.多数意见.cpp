#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <vector>

using namespace std;

const int N = 1e5 + 10;
vector<int> p[N];

int main()
{
    int t;
    scanf("%d", &t);
    while (t--)
    {
        int n;
        scanf("%d", &n);
        for (int i = 1; i <= n; i++)
            p[i].clear();
        for (int i = 1; i <= n; i++)
        {
            int h;
            scanf("%d", &h);
            p[h].push_back(i);
        }
        int cnt = 0;
        for (int i = 1; i <= n; i++)
        {
            for (int j = 0; j + 1 < p[i].size(); j++)
            {
                if (p[i][j + 1] - p[i][j] <= 2)
                {
                    cnt++;
                    printf("%d ", i);
                    break;
                }
            }
        }
        if (!cnt)
            printf("-1");
        puts("");
    }

    return 0;
}