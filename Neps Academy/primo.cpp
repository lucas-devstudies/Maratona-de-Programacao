#include <iostream>

using namespace std;

bool eh_primo(int x){
    int cont=0;
    if (x==0)
    {
        return false;
    }
	for(int i=1;i<=x;i++){
	    if (x%i==0)
	    {
	        cont++;
	    }
	}
	if(cont>2 || cont==1)
	{
        return false;
	}
	else
	{
	    return true;
	}
}

int main(){
	int x;

	cin>>x;

	if(eh_primo(x)){
		cout << "S" << "\n";
	}else{
		cout << "N" << "\n";
	}
}