#include<bits/stdc++.h>
#include<vector>
#include<algorithm>
using namespace std;
int main(){
    int n,s;
    vector<int> numeros(12,0);
    cin>>n;

    for(int i=0;i<n;i++)
    {
        cin>>s;
        numeros[s-1] ++;
    }
    auto t = max_element(numeros.begin(),numeros.end());
    for(int i=0;i<n;i++)
    {
        if(numeros[i] == *t)
        {
            cout<<
        }
    }
}