#include <iostream>
using namespace std;
int main()
{
    float a,m,media;
    cin>>a>>m;
    media = (a+m)/2;
    if (media>=7)
    {
        cout<<"Aprovado";
    }
    else if(media>=4 and media<7)
    {
        cout<<"Recuperacao";
    }
    else
    {
        cout<<"Reprovado";
    }
    return 0;
}
