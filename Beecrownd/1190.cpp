#include<bits/stdc++.h>
#include<iomanip>
using namespace std;
int main(){
    char o;
    int v=3;
    int t = (v/4) - (v/2);
    double n;
    double m[v][v];

    cin>>o;
    for(int i=0; i<v; i++){
        for(int j=0; j<v; j++){
            cin >> m[i][j];
            if (j>((v-1)-i) && j>i){
                n += m[i][j];
            }
        }
    }
    cout << fixed << setprecision(1);
    if(o == 'S'){
        cout<<n<<endl;
    } else{
        cout<<n/t<<endl;
    }
}