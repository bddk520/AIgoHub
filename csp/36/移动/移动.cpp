#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>

using namespace std;

const int N = 105;

int n;

void solution(int x, int y, char op[N])
{
    for (int j = 0; op[j]; j++)
    {
        if (op[j] == 'f')
        {
            if (y < n)
                y += 1;
        }
        else if (op[j] == 'b')
        {   
            if (y > 1)
                y -= 1;
        }
        else if (op[j] == 'l')
        {
            if (x > 1)
                x -= 1;
        }
        else
        {
            if (x < n)
                x += 1;
        }
    }
    cout << x << ' ' << y << endl;
}

int main()
{
    int k;
    cin >> n >> k;
    for (int i = 0; i < k; i++)
    {
        int x, y;
        char op[N];
        cin >> x >> y >> op;
        solution(x, y, op);
    }
}