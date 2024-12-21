#include <iostream>
using namespace std;
int main()
{
    int p,q,n,s;
    char c;
    cin>>n;
    cin>>p>>c>>q;
    if (c=='*')
    {
        s = p*q;
        if (s<=n)
        {
            cout<<"OK";
        }
        else
        {
            cout<<"OVERFLOW";
        }
    }
    else if (c=='+')
    {
        s = p+q;
        if (s<=n)
        {
            cout<<"OK";
        }
        else
        {
            cout<<"OVERFLOW";
        }
    }
    else if (c=='-')
    {
        s = p-q;
        if (s<=n)
