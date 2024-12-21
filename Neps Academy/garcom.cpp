#include<iostream>
using namespace std;
int main(){
    int n;
    int a,b,copos=0;
    
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>a>>b;
        if (a>b)
        {
            copos+=b;
        }
    }
    cout<<copos<<endl;
}