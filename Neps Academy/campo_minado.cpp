#include<iostream>
#include<vector>
using namespace std;
int main()
{
    int n,s,c;
    cin>> n;

    vector<int> l;
    vector<int> saida;
    for(int i=0;i<n;i++)
    {
        cin>>s;
        l.push_back(s);
    }
    for(int i=0;i<n;i++)
    {
        c=0;
        if(l[i]==1)
        {
            c++;
        }
        if(i<n-1)
        {
            if(l[i+1]==1)
            {
                c++;
            }
        }
        if(i!=0)
        {
            if(l[i-1]==1)
            {
                c++;
            }
        }
        saida.push_back(c);
    }
    for(int j=0;j<n;j++)
    {
        cout<<saida[j]<<endl;
    }
    return 0;
}