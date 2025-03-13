#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

const int N = 1e5 + 10;

int son[N][26], idx, cnt[N];
char s[N];

void insert(char str[])
{
    int p = 0;
    for (int i = 0; str[i]; i++)
    {
        int u = str[i] - 'a';   
        if (!son[p][u])
            son[p][u] = ++idx;//注意这里是
        p = son[p][u];
    }
    cnt[p]++;
}

int query(char str[])
{
    int p = 0;
    for (int i = 0; str[i]; i++)
    {
        int u = str[i] - 'a';
        if (!son[p][u])
            return 0;
        p = son[p][u];
    }
    return cnt[p];
}

int main()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        char op[2];
        cin >> op >> s;
        if (strcmp(op, "I") == 0)
        {
            insert(s);
        }
        else
        {
            int res = query(s);
            cout << res << endl;
        }
    }
    return 0;
}