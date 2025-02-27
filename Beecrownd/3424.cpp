#include<bits/stdc++.h>
#include<string>
using namespace std;
int main(){
    int n;
    bool erro = false;
    while(cin>>n){
        if (n==9){
            erro = true;
        }
    }
    if (erro ==  true) cout<<"F"<<endl;
    else cout<<"S"<<endl;
    return 0;
}