#include<bits/stdc++.h>
using namespace std;
int main(){
    vector<pair<int,int>> v = { {10,1},{12,3},{2,5}};

    v.push_back({5,3});
    cout<<v[3].first<<endl;
}