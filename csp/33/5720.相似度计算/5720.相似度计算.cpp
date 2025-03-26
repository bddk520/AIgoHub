// #include <iostream>
// #include <cstring>
// #include <algorithm>
// #include <cctype>
// #include <string>
// #include <unordered_map>

// using namespace std;

// const int N = 1e4 + 10;

// string a[N], b[N];

// int main()
// {
//     int n, m;
//     cin >> n >> m;
//     unordered_map<string, int> amap;
//     unordered_map<string, int> bmap;
//     unordered_map<string, int> cmap;
//     for (int i = 1; i <= n; i++)
//     {
//         cin >> a[i];
//         for (int j = 0; j < a[i].size(); j++)
//         {
//             a[i][j] = tolower(a[i][j]);
//         }
//         amap[a[i]] = 1;
//     }
//     for (int i = 1; i <= m; i++)
//     {
//         cin >> b[i];
//         for (int j = 0; j < b[i].size(); j++)
//         {
//             b[i][j] = tolower(b[i][j]);
//         }
//         bmap[b[i]] = 1;
//     }
//     int res = 0;
//     for (const auto &paira : amap)
//     {
//         cmap[paira.first] = paira.second;
//     }
//     for (const auto &pairb : bmap)
//     {
//         cmap[pairb.first] = pairb.second;
//     }
//     cout << amap.size() + bmap.size() - cmap.size() << endl
//          << cmap.size() << endl;
//     return 0;
// }

#include <iostream>
#include <algorithm>
#include <set>
#include <string>

using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;
    set<string> a;
    set<string> b;
    for (int i = 0; i < n; i++)
    {
        string s;
        cin >> s;
        for (int j = 0; j < s.size(); j++)
            s[j] = tolower(s[j]);
        a.insert(s);
    }
    for (int i = 0; i < m; i++)
    {
        string s;
        cin >> s;
        for (int j = 0; j < s.size(); j++)
            s[j] = tolower(s[j]);
        b.insert(s);
    }
    set<string> c;
    set_intersection(a.begin(), a.end(), b.begin(), b.end(), inserter(c, c.begin()));

    cout << c.size() << endl
         << a.size() + b.size() - c.size() << endl;

    return 0;
}