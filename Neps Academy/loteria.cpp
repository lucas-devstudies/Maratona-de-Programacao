#include<bits/stdc++.h>
#include<sstream>
using namespace std;
int main(){
    int n,c=0;
    vector<int> selecionados;
    string txt;

    getline(cin,txt);
    istringstream stream(txt);

    while(stream>>n){
        selecionados.push_back(n);
    }
    while(cin>>n){
        for(int j:selecionados){
            if (n==j){
                c++;
            }
        }
    }
    if (c<=2){
        cout<<"azar"<<endl;
    }
    else if(c==3){
        cout<<"terno"<<endl;
    }
    else if(c==4){
        cout<<"quadra"<<endl;
    }
    else if(c==5){
        cout<<"quina"<<endl;
    }
    else{
        cout<<"sena"<<endl;
    }
}