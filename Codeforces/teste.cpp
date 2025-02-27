#include<bits/stdc++.h>
#include<cmath>
#include<iomanip>
using namespace std;
int main(){
    double a,b,c;
    double delta;
    cin>>a>>b>>c;
    if (a==0 && b==0 && c==0){
        exit(0);
    }
    else{
        if (a==0 || b==0 || c==0){
            cout<<"Impossivel de calcular"<<endl;
        }else{
            delta = (b*b)-(4*a*c);
            double r1 = (-b+sqrt(delta))/(2*a);
            double r2 = (-b-sqrt(delta))/(2*a);
            cout<<fixed<<setprecision(5);
            cout<<"R1 = "<<r1<<endl;
            cout<<"R2 = "<<r2<<endl;
        }
    }
    return 0;
}