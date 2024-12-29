#include<bits/stdc++.h>
#include<vector>
using namespace std;
int main(){
    int n,x,v_size,muro,p,m,g;
    cin>>n>>x;
    cin.ignore();
    int h,c=0;

    bool passou = false;
    
    char s[n+1];
    cin.getline(s, n+1);
    
    cin>>p>>m>>g;
    vector<int> v;

    for(int i=0;i<n;i++){
        if(s[i]=='P'){
            muro = p;
        }
        else if(s[i]=='M'){
            muro = m;
        }
        else{
            muro = g;
        }
        passou = false;
        v_size = v.size();
        
        for(int j=0;j<v_size;j++){
            if (v[j]>=muro){
                v[j] = v[j]-muro;
                passou = true;
                break;
            }
        }
        if (passou != true){
            c+=1;
            h = x-muro;
            if (h>=p){
                v.push_back(h);
            }
        }
    }
    cout<<c<<endl;

    return 0;
}


    