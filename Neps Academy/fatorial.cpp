#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,s=1;
    cin>>n;
    for(int i=1;i<n+1;i++)
    {
        s = s * i;
    }
    cout<<s<<endl;
}