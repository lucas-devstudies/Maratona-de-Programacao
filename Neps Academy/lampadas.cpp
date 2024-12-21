#include<iostream>
using namespace std;
int main()
{
    int n,y;
    bool c1=false,c2=false;
    cin>>n;
    for (int i = 0; i <n; i++)
    {
        cin>>y;
        if (y==1)
        {
            c1 = !c1;
        }
        else{
            c1 = !c1;
            c2 = !c2;
        }
    }
    if (c1==true){
        cout<<1<<endl;
    }
    else{
        cout<<0<<endl;
    }
    if (c2==true){
        cout<<1<<endl;
    }
    else{
        cout<<0<<endl;
    }
    return 0;
}
