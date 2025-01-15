#include<bits/stdc++.h>
using namespace std;

int numeros_triangulares(int x,int n){
    int v = (n*(n+1))/2;
    if (v==x){
        return n;
    }else if(v>x){
        return n-1;
    }else{
        numeros_triangulares(x,n+1);
    }
}

int main(){
    int t,v;
    
    cin>>t;
    for(int i=0;i<t;i++){
        cin>>v;
        cout<<(numeros_triangulares(v,1))<<endl;;
    }

    return 0;
}