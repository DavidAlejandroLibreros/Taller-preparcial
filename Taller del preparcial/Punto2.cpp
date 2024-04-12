#include <iostream>

using namespace std;

int main() {
int Numero1,Numero2,Numero3;

cout << "Introduce el primer numero: ";
cin >> Numero1;

cout << "Introduce el segundo numero: ";
cin >> Numero2;

cout << "Introduce el tercer numero: ";
cin >> Numero3;

if ( Numero1 > Numero2 && Numero1 > Numero3){

cout << "El número mayor es " << Numero1;

}
else if (Numero2 > Numero3 ){

cout << "El número mayor es " << Numero2;

}

else {

cout << "El número mayor es " << Numero3;


}




}