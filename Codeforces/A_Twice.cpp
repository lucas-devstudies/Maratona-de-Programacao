#include<bits/stdc++.h>
using namespace std;
int main(){
    int t,n,v;

    cin>>t;
    for(int i=0;i<t;i++){
        int p = 0;
        cin>>n;
        vector<int> v1(n,0);

        for(int j=0;j<n;j++){
            cin>>v;
            v1[v-1]+=1;
        }
        for(int i=0;i<n;i++){
            p+=(v1[i]/2);
        }
        cout<<p<<endl;
    }
    return 0;
}