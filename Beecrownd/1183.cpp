#include<bits/stdc++.h>
#include<iomanip>
using namespace std;
int main(){
    char o;
    int v=12;
    int t = ((v*v)-v)/2;
    double n;
    double m[v][v];

    cin>>o;
    for(int i=0; i<v; i++){
        for(int j=0; j<v; j++){
            cin >> m[i][j];
            if (j>i){
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