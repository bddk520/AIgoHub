// #include <iostream>
// #include <algorithm>
// #include <cstring>
// #include <cstdio>
// #include <unordered_map>

// using namespace std;

// const int M = 3 * 1e5 + 10;

// typedef struct node
// {
//     int left;
//     int right;
//     int value;
// } node;

// unordered_map<int, node> a;

// void dfs(int p)
// {

//     if (a[p].value >= 5)
//     {
//         int left = a[p].left, right = a[p].right;
//         a.erase(p);
//         a[left].right = right;
//         a[right].left = left;
//         a[left].value += 1;
//         a[right].value += 1;
//         dfs(left);
//         dfs(right);
//     }
// }

// int main()
// {
//     int c, m, n;
//     cin >> c >> m >> n;
//     int l = 0, r = 0;
//     for (int i = 0; i < m; i++)
//     {
//         int x, w;
//         cin >> x >> w;
//         a[x].value = w;
//         a[x].left = l;
//         a[l].right = x;
//         l = x;
//         r = x;
//     }
//     for (int i = 0; i < n; i++)
//     {
//         int p;
//         cin >> p;
//         a[p].value += 1;
//         dfs(p);
//         cout << a.size() << endl;
//     }

//     return 0;
// }
#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <unordered_map>
#include <vector>
#include <map>
using namespace std;

const int M = 3 * 1e5 + 10;

typedef struct node
{
    int left;
    int right;
    int value;
    bool st;
} node;

unordered_map<int, node> a;
 int res ;
void dfs(int p)
{
    // if (!a[p].st)
    //     return;
    // for(const auto& pair:a)
    // {
    //     cout << pair.first <<' ' << pair.second.value <<  endl;
    // }
    // cout << "-----" << endl;
    if (a[p].value >= 5)
    {
        int left = a[p].left, right = a[p].right;
        a[p].st = false;
        res --;
        if (left != 0)
        {
            a[left].right = right;
            a[left].value += 1;
        }
        if (right != 0)
        {
            a[right].left = left;
            a[right].value += 1;
        }
        if (left != 0)
            dfs(left);
        if (right != 0 && a[right].st)
            dfs(right);
    }
}

int main()
{
    int c, m, n;
    cin >> c >> m >> n;
    // int l = 0, r = 0;
    vector<int> pos;
    for (int i = 0; i < m; i++)
    {
        int x, w;
        cin >> x >> w;
        a[x].value = w;
        a[x].st = true;
        pos.push_back(x);
    }
   res= m;
    sort(pos.begin(), pos.end());
    int size = pos.size();
    for (int i = 0; i < size; i++)
    {
        int x = pos[i];
        if (i > 0)
            a[x].left = pos[i - 1];
        if (i < size - 1)
            a[x].right = pos[i + 1];
    }
    // for(const auto& pair:a)
    // {
    //     cout << pair.first <<' ' << pair.second.value << ' ' << pair.second.left << ' ' << pair.second.right << ' ' << endl;
    // }
    // cout << "-----" << endl;
    for (int i = 0; i < n; i++)
    {
        int p;
        cin >> p;
        a[p].value += 1;
        dfs(p);
        cout <<res << endl;
        // for(const auto& pair:a)
        // {
        // cout << pair.first <<' ' << pair.second.value <<  endl;
        // }
        // cout << "*******" << endl;
    }

    return 0;
}
    