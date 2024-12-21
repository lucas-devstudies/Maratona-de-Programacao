#include<iostream>
using namespace std;
int main()
{
    int n,s,total=0,v2=2,v3=2;
    cin>>n;
    for (int i=0;i<n;i++)
    {
        cin>>s;
        if (i==0)
        {
            v3 = s;
        }
        else if(i==1)
        {
            v2 = s;
        }
        else if(s == 0 && v2==0 && v3==1)
        {
            total++;
            v3 = v2;
            v2 = s;
        }
        else
        {
            v3 = v2;
            v2 = s;
        }
    }
    cout<<total<<endl;
}