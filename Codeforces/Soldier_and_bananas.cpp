#include <bits/stdc++.h>
using namespace std;
int main()
{
    int k,s=0,n=0,w;
    scanf("%d %d %d",&k,&n,&w);
    for (int i =1; i<w+1; i++)
    {
        s += k*i;
    }
    if (s-n<=0)
    {
        cout<<0;
    }
    else{
        cout<<s-n;
    }
    return 0;
}
