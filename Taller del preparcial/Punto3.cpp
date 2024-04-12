#include <iostream>
#include <cmath>

using namespace std;

int main() {
    double Numero_decimal;

    cout << "Introduce un numero decimal: ";
    cin >> Numero_decimal; 

    double Valor_a = fabs(Numero_decimal);

    if (Numero_decimal == 0) {
        cout << "0";
    }
    else if (Numero_decimal > 0) {
        cout << "El número es positivo" << endl;
        if (Valor_a < 1){
            cout << " y es pequeño";
        }
        else if (Valor_a > 1000000){
                cout << " y es grande";
        } 
    }
    else{
        cout << "El número es negativo" << endl;
        if (Valor_a < 1){
            cout << " y es pequeño";}
        else if (Valor_a > 1000000){
            cout << " y es grande";}
    }

    
}