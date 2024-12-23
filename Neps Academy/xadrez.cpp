#include<bits/stdc++.h>
using namespace std;
int main()
{
    int l,c;
    
    cin>>l;
    cin>>c;
    if (l==c)
    {
        cout<<"1"<<endl;
    }
    else if(l%2==0 && c%2==0)
    {
        cout<<"1"<<endl;
    }
    else if(l%2==0 && c%2!=0)
    {
        cout<<"0"<<endl;
    }
    else if(l%2!=0 && c%2==0)
    {
        cout<<"0"<<endl;
    }
    else if(l%2!=0 && c%2!=0)
    {
        cout<<"1"<<endl;
    }
}