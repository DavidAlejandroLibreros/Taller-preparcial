#include <iostream>
using namespace std;

int main(){

string Lista_Ovejas[5] = { "Oveja1" , "Oveja2" , "Oveja3" , "Oveja4" , "Oveja5" };

int Contador_ovejas = 1;

while (Contador_ovejas < 6){

    cout << "La oveja número: " << Contador_ovejas << " llamada: " << Lista_Ovejas[Contador_ovejas - 1] << " se encuentra aquí" << endl;
    Contador_ovejas ++;
}
cout << "Todas las ovejas se encuentran aquí" ;

}
