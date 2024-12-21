#include <iostream>
using namespace std;
int main()
{
    int n1,n2;
    cin>>n1>>n2;
    float media = (n1*2+n2*3)/5;
    if (media>=7)
    {
        cout<<"Aprovado";
    }
    else if(media<3)
    {
        cout<<"Reprovado";
    }
    else
    {
        cout<<"Final";
    }
    return 0;
}
