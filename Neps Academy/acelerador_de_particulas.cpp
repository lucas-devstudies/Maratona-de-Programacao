#include <iostream>
using namespace std;
int main()
{
    int n1,s;
    cin>>n1;
    s = n1%8;
    if (s==6)
    {
        cout<<1<<endl;
    }
    else if(s==7)
    {
         cout<<2<<endl;
    }
    else
    {
         cout<<3<<endl;
    }
    return 0;
}
