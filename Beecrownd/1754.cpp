#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long x,y,h;
    int t;
    
    cin>>t;
    for(int i=0;i<t;i++){
        cin>>x>>y;
        h = x/y;
        if(x%y==0){
            cout<<h<<endl;
        }
        else if(y>=x){
            cout<<2<<endl;
        }
        else{
            cout<<h+1<<endl;
        }
    }
    
    return 0;
}