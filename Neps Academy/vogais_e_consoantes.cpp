#include <bits/stdc++.h>
using namespace std;

int main() {
    int c, v, t;
    char txt[256];
    vector<char> consoantes;
    vector<char> vogais;

    cin.getline(txt, 256);

    t = strlen(txt); 

    for (int i = 0; i < t; i++) {
        char ch = txt[i];
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' || ch=='A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U') {
            vogais.push_back(txt[i]);
        } else if (isalpha(ch)){
            consoantes.push_back(txt[i]);
        }
    }

    cout << "Vogais: ";
    v = vogais.size();
    for (int i = 0; i < v; i++) {
        cout << vogais[i];
    }
    cout << endl;

    cout << "Consoantes: ";
    c = consoantes.size();
    for (int i = 0; i < c; i++) {
        cout << consoantes[i];
    }

    return 0;
}
