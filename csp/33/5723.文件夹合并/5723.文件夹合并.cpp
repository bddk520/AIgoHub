#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>

using namespace std;

const int N = 5 * 1e5 + 10;

int e[N], ne[N], h[N], idx;
int w[N], st[N], son[N];

int n, m;

void add(int a, int b)
{
    e[idx] = b;
    ne[idx] = h[a];
    // cout << idx << ' ' << e[idx] << ' ' << ne[idx] << ' ' << endl;
    h[a] = idx++;
}

void merge(int x)
{
    for (int i = h[x]; i != -1; i = ne[i])
    {
        int t = e[i];
        // cout << t << endl;
        if (!st[t])
            continue;
        st[t] = 0;
        w[x] += w[t];
        son[x] -= 1;
        for (int j = h[t]; j != -1; j = ne[j])
        {
            int tt = e[j];
            if (!st[tt])
                continue;
            add(x, tt);
            // cout << x << "->" << j;
            son[x] += 1;
        }
    }
}

int bfs(int x)
{

    if (x == 1)
        return 1;
    int q[N], hh = 0, tt = -1;
    q[++tt] = 1;
    int dist[N];
    dist[1] = 1;
    while (hh <= tt)
    {
        int t = q[hh++];
        // cout << t << endl;
        for (int i = h[t]; i != -1; i = ne[i])
        {
           
            int nex = e[i];
            // cout << nex << endl;
            dist[nex] = dist[t] + 1;
            if (!st[nex])
                continue;
            
            if (nex == x)
                return dist[nex];
            q[++tt] = nex;
        }
    }
}

int main()
{

    cin >> n >> m;
    for(int i = 0; i <= n;i++)h[i] = -1;
    for (int i = 2; i <= n; i++)
    {
        int f;
        cin >> f;
        add(f, i);
        son[f] += 1;
    }
    for (int i = 1; i <= n; i++)
    {
        cin >> w[i];
        st[i] = 1;
        
    }
    
    for (int i = 0; i < m; i++)
    {
        int op, x;
        cin >> op >> x;
        if (op == 1)
        {
            merge(x);
            cout << son[x] << ' ' << w[x] << endl;
        }
        else
        {
          
            cout << bfs(x) << endl;
        }
        // cout << "---" << endl;
    }
    return 0;
}