#include <iostream>
using namespace std;
int main()
{
    int p1,c1,p2,c2;
    int t1,t2;
    cin>>p1>>c1>>p2>>c2;
    t1 = p1*c1;
    t2 = p2*c2;
    if (t1 == t2)
    {
        cout<<0;
    }
    else if(t1>t2)
    {
        cout<<-1;
    }
    else
    {
        cout<<1;
    }
    return 0;
}
