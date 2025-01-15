#include<bits/stdc++.h>
#include<iomanip>
using namespace std;
int main(){
    int n,v = 3;
    double r=0;
    char operacao;
    double m[v][v];

    cin>> n;
    cin>> operacao;
    for(int i=0;i<v;i++){
        for(int j=0;j<v;j++){
            cin>> m[i][j];
        }
    }
    for(int i=0;i<v;i++){
        r += m[i][n];
    }
    cout<<fixed<<setprecision(1);
    if(operacao == 'S'){
        cout<<r<<endl;
    }else{
        cout<<(r/v)<<endl;
    }
}