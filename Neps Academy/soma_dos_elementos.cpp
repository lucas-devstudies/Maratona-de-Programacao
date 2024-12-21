#include <iostream>
using namespace std;
 
int main() {
    int n,s,soma=0;
    
    cin>>n;
    for(int i=0; i<n;i++)
    {
        cin>>s;
        soma += s;
    }
    printf("%d",soma);
    
    return 0;
}