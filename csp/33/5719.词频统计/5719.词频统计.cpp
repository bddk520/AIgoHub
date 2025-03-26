#include<iostream>
#include<algorithm>
#include<cstring>

using namespace std;

const int N = 105;

int cnt[N][N],sum[N];

int main()
{
    int n, m;
    cin >> n >> m;
    for(int i = 1;i <=n;i++)
    {
        int l ;
        cin >> l;
        for(int j = 0;j < l;j++)
        {
            int s;
            cin >> s;
            sum[s] += 1;
            cnt[s][i] = 1;
        }
    }
    for(int i = 1;i <= m;i++)
    {
        int res = 0;
        for(int j = 1;j <= n;j++)
        {
            if(cnt[i][j]) res += 1;
        }
        cout << res << " " << sum[i] << endl;
    }
    return 0;
}