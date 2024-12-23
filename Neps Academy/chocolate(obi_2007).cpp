#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,t,s=0;
    
    cin>>t;
    for(int i=0;i<t;i++)
    {
        cin>>n;
        s+=(n-1);
    }
    cout<<s<<endl;
}