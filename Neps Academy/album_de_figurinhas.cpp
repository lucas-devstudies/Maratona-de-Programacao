#include<bits/stdc++.h>
#include<vector>
using namespace std;
int main(){
    int n, c=0,m,s;
    
    cin>>n;
    cin>>m;
    vector<int> v;
    for(int i=0;i<n;i++)
    {
        v.push_back(0);
    }
    for(int i=0;i<m;i++)
    {
        cin>>s;
        if (v[s-1] == 0)
        {
            v[s-1] = 1;
            c++;
        } 
    }
    cout<<n-c<<endl;
}
