#include<bits/stdc++.h>
using namespace std;
bool diagonal(int matriz[3][3]){
    int v = matriz[0][0]+matriz[1][1]+matriz[2][2];
    int h = matriz[0][2]+matriz[1][1]+matriz[2][0];
    if (h==v){
        return true;
    }
    return false;
}
bool linhas(int matriz[3][3]){
    int s = 0;
    for (int i = 0; i<3; i++){
        int s1 = 0;
        for(int j=0; j<3; j++){
            if (i==0){
                s += matriz[i][j];
            } else{
                s1 += matriz[i][j];
            }
        }
        if (i>0){
            if (s1 != s){
                return false;
            }
        }
    }
    return true;
}
bool colunas(int matriz[3][3]){
    int s = 0;
    for (int i = 0; i<3; i++){
        int s1 = 0;
        for(int j=0; j<3; j++){
            if (i==0){
                s += matriz[j][i];
            } else{
                s1 += matriz[j][i];
            }
        }
        if (i>0){
            if (s1 != s){
                return false;
            }
        }
    }
    return true;
}

int main(){
    int m[3][3];
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            cin>>m[i][j];
        }
    }
    if (diagonal(m) == false || colunas(m) == false || linhas(m) == false){
        cout<<"NAO"<<endl;
    }
    else{
        cout<<"SIM"<<endl;
    }
}