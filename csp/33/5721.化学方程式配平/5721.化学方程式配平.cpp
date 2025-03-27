#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <unordered_map>
#include <vector>
#include <string>
#include <cctype>
#include <set>
#include <cmath>

using namespace std;

const int N = 45;
const double eps = 1e-8;
// unordered_map<string,vector>faction;
typedef pair<string, int> PSI;

int n, m;

int s2digit(const string &s)
{
    int res = 0;
    for (int i = 0; i < s.size(); i++)
    {
        res = s[i] - '0' + res * 10;
    }
    return res;
}

void gauss(double fac[N][N], int num)
{
    int c, r;
    for (c = 0, r = 0; c < m; c++)
    {
        int t = r;
        for (int i = r; i < num; i++)
        {
            if (fabs(fac[i][c]) > fabs(fac[t][c]))
                t = i;
        }
        if (fabs(fac[t][c]) < eps)
            continue;

        for (int i = c; i < m; i++)
            swap(fac[t][i], fac[r][i]);
        for (int i = m - 1; i >= c; i--)
            fac[r][i] /= fac[r][c];
        for (int i = r + 1; i < num; i++)
        {
            if (fabs(fac[i][c]) > eps)
            {
                for (int j = m - 1; j >= c; j--)

                    fac[i][j] -= fac[i][c] * fac[r][j];
            }
        }
        r++;
    }
    // for (int i = 0; i < num; i++)
    //     {
    //         for (int j = 0; j < m; j++)
    //         {
    //             cout << fac[i][j] << ' ';
    //         }
    //         cout << endl;
    //     }
    // if(r < m) cout << r << ' ' << m << ' ' <<   'Y' << endl;
    // else cout << r << ' ' << m << ' ' <<  'N' << endl;
    if (r < m)
        cout << 'Y' << endl;
    else
        cout << 'N' << endl;
}

int main()
{
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        unordered_map<string, int> wuzi[N];
        set<string> yuansu;
        cin >> m;
        for (int j = 0; j < m; j++)
        {
            string s;
            cin >> s;
            for (int k = 0; k < s.size(); k++)
            {
                string elm;
                while (isalpha(s[k]))
                {
                    elm += s[k];
                    k++;
                }
                yuansu.insert(elm);

                string digit;
                while (isdigit(s[k]))
                {
                    digit += s[k];
                    k++;
                }
                wuzi[j][elm] = s2digit(digit);
                k = k - 1;
            }
        }
        double fac[N][N];
        memset(fac, 0, sizeof(fac));
        int j = 0;
        for (auto it = yuansu.begin(); it != yuansu.end(); j++, it++)
        {
            for (int k = 0; k < m; k++)
            {
                if (wuzi[k].find(*it) != wuzi[k].end())
                {
                    fac[j][k] = wuzi[k][*it];
                    // cout << *it << ' ' << wuzi[k][*it] << ' ' << k << ' ' << endl;
                }
                else
                {
                    fac[j][k] = 0;
                    //  cout << *it << ' ' << fac[j][k] << ' ' << k << ' ' << endl;
                }
            }
        }

        // for (int i = 0; i < yuansu.size(); i++)
        // {
        //     for (int j = 0; j < m; j++)
        //     {
        //         cout << fac[i][j] << ' ';
        //     }
        //     cout << endl;
        // }

        gauss(fac, yuansu.size());
        // cout << "-------" << endl;
    }
    return 0;
}