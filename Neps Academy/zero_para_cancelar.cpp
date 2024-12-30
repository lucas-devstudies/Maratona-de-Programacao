#include<bits/stdc++.h>
#include<vector>
using namespace std;
int main(){
    int n,s,soma=0;
    vector<int> valores;
    
    cin>>n;
    
    for(int i=0;i<n;i++){
        cin>>s;
        if (s == 0){  
            if (!valores.empty()){
                valores.pop_back();
            }
            else{
                continue;
            }
        }
        else{
            valores.push_back(s);
        }
    }
    for(int i=0;i<(int)valores.size();i++){
        soma+=valores[i];
    }
    cout<<soma<<endl;
}