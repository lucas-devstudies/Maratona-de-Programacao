#include<iostream>
using namespace std;
int main(){
    int ps=0,m;
    char n;
    int t;

    cin>>t;
    for(int i=0;i<t;i++){
        cin>>n>>m;
        if (n=='P'){
            ps+=m;
        } else{
            if (ps<m){
                cout<<"YES"<<endl;
            }else{
                cout<<"NO"<<endl;
            }
            ps=ps-m;
            if (ps<0){
                ps=0;
            }
        }
    }

    return 0;
}