#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

const int N = 20000 + 10, M = 26;

int cnt[M][M], st[M][M];
char s[N];
int n, f;

void update(int l, int r, int v)
{
    l = max(0, l);
    r = min(r, n - 1);
    for (int i = l; i + 2 <= r; i++)
    {
        int a = s[i], b = s[i + 1], c = s[i + 2];
        if (a != b && b == c)
        {
            cnt[a][b] += v;
        }
        if (cnt[a][b] >= f)
            st[a][b] = 1;
    }
}

int main()
{

    scanf("%d%d%s", &n, &f, &s);
    for (int i = 0; i < n; i++)
        s[i] = s[i] - 'a';
    update(0, n - 1, 1);
    for (int i = 0; i < n; i++)
    {
        char t = s[i];
        update(i - 2, i + 2, -1);
        for (int j = 0; j < 26; j++)
        {
            if (j != t)
            {
                s[i] = j;
                update(i - 2, i + 2, 1);
                update(i - 2, i + 2, -1);
            }
        }
        s[i] = t;
        update(i - 2, i + 2, 1);
    }
    int res = 0;
    for (int i = 0; i < 26; i++)
    {
        for (int j = 0; j < 26; j++)
        {
            if (st[i][j])
                res += 1;
        }
    }
    printf("%d\n", res);
    for (int i = 0; i < 26; i++)
    {
        for (int j = 0; j < 26; j++)
        {
            if (st[i][j])
            {
                printf("%c%c%c\n", 'a' + i, 'a' + j, 'a' + j);
            }
        }
    }

    return 0;
}
