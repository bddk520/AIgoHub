#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        string s;
        cin >> s;
        if (s.back() == '0')
            printf("E\n");
        else
            printf("B\n");
        
    }
    return 0;
}