#include <iostream>

using namespace std;

int main(){
    int n=0,soma=0,a,v;
    cin>>a;
    while(soma<1000000)
    {
        cin>>v;
        n+=1;
        soma+=v;
    }
    printf("%d",n);
    return 0;
}
