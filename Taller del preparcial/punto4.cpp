#include <iostream>

using namespace std;

int main() {
    int Num_usuario;
    cout << "Introduce tu número de usuario (1-7): ";
    cin >> Num_usuario; 

        switch (Num_usuario){
            case 1: 
                cout << "El día es lunes" << endl;
                break;
            case 2:
                cout << "El día es martes" << endl; 
                break;
            case 3:
                cout << "El día es miércoles" << endl;
                break;
            case 4:
                cout << "El día es jueves" << endl;
                break;
            case 5:
                cout << "El día es viernes" << endl;
                break;
            case 6:
                cout << "El día es sábado" << endl;
                break;
            case 7:
                cout << "El día es viernes" << endl;
                break;

        }
return 0;

}