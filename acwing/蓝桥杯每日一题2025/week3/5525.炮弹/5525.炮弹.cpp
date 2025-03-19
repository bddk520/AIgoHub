#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

const int N = 1e5 + 10;
int q[N], v[N];

int main()
{
    int n, s, flag = 0;
    scanf("%d%d", &n, &s);
    for (int i = 1; i <= n; i++)
    {
        scanf("%d%d", &q[i], &v[i]);
        if (q[i])
            flag++;
    }
    int cnt = 0;
    int V = 1;
    int jump = 0;
    while (s >= 1 && s <= n && flag != cnt)
    {
        if (jump < 1e5)
        {
            jump += 1;
        }
        else
        {
            break;
        }
        if (q[s] == 1)
        {
            if (abs(V) >= v[s])
            {
                q[s] = -1;
                cnt += 1;
                s += V;
            }
            else
            {
                s += V;
            }
        }
        else if (q[s] == 0)
        {
            if (V > 0)
            {
                V = -(V + v[s]);
            }
            else
            {
                V = -(V - v[s]);
            }
            s += V;
        }
        else if (q[s] == -1)
        {
            s += V;
        }
    }
    printf("%d", cnt);
    return 0;
}