#include<bits/stdc++.h>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
    int n,p,imp;
    vector<int> pares;
    vector<int> impares;

    for(int i=0;i<10;i++){
        cin>>n;
        if (n%2 == 0){
            pares.push_back(n);
        }
        else{
            impares.push_back(n);
        }
    }
    p = pares.size();
    for(int i = 0;i<p;i++){
        if(i==0)
        {
            cout<<pares[i];
        }   
        else{
            cout<<" "<<pares[i];
        }
    }
    cout<<endl;
    imp = impares.size();
    for(int i = 0;i<imp;i++) {
        if(i==0)
        {
            cout<<impares[i];
        }   
        else{
            cout<<" "<<impares[i];
        }
    }
    cout<<endl;
    return 0;
}