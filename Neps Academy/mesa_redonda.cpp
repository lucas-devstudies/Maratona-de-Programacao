#include<bits/stdc++.h>
#include<vector>
using namespace std;
int main(){
    vector<int> assentos = {0,0,0};
    int a,b;
    cin>>a;
    cin>>b;

    if(a%3 == 0){
        assentos[0]=1;
    }
    else if(a%3 == 1){
        assentos[1]=1;
    }
    else if(a%3 == 2){
        assentos[2]=1;
    }
    
    if (b%3 == 0){
        if(assentos[0] == 1){
            assentos[1]=1;
        }
        else{
            assentos[0]=1;
        }
    }
    else if(b%3 == 1){
        if(assentos[1] == 1){
            assentos[2]=1;
        }
        else{
            assentos[1]=1;
        }
    }
    else if(b%3 == 2){
        if(assentos[2] == 1){
            assentos[0]=1;
        }
        else{
            assentos[2]=1;
        }
    }
    for(int i=0;i<3;i++){
        if(assentos[i]==0){
            cout<<i<<endl;
        }
    }
    return 0;
}