#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,m;
    cin>>n;
    cin>>m;
    if (n<m)
    {
        for(int i=n;i<m+1;i++)
        {
            if (i==n)
            {
                cout<<i;
            }
            else{
                cout<<" "<<i;
            }
        }
    }
    else if(m<n)
    {
        for(int i=m;i<n+1;i++)
        {
            if (i==m)
            {
                cout<<i;
            }
            else{
                cout<<" "<<i;
            }
        }
    }
    else{
        cout<<m;
    }
    
    cout<<endl;
}