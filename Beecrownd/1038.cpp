#include <iostream>
using namespace std;
 
int main() {
    int c,qtd;
    float total;
    
    cin>>c>>qtd;
    
    if(c==1)
    {
        total = 4.00*qtd;
    }
    else if (c==2)
    {
        total = 4.50*qtd;
    }
    else if (c==3)
    {
        total = 5.00*qtd;
    }
    else if(c==4)
    {
        total = 2.00*qtd;
    }
    else
    {
        total= 1.50*qtd;
    }
    printf("Total: R$ %.2f\n",total);
    
    return 0;
}