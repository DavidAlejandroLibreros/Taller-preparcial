#include <iostream>
#include <fstream>
using namespace std;

    class Cuenta{
        private:
        double saldo;
        void registrartransacciones(string tipo, double cantidad){
            ofstream archivo("Transacciones.txt", ios::app);
            if (archivo.is_open()){
                archivo << tipo << ": " << ", Saldo: " << cantidad << endl;
                archivo.close();
            }else{
                cout << "No se pudo abrir el archivo de transacciones" << endl;

            }
            
            
            }

        public:
            Cuenta(){
                saldo = 0,0;
            }
            Cuenta(double saldo_inicial){
                saldo = saldo_inicial;

            }
        
        void Retirar(double saldo_retirado){
            if(saldo_retirado > saldo){
                cout << "Saldo insuficiente." << endl;
                registrartransacciones("Retiro: ", saldo_retirado);

            } else{
            saldo = saldo - saldo_retirado;
            }}
        void Depositar(double saldo_ingresado){
            if(saldo_ingresado < 0){
                cout << "No puede ingresar un saldo negativo" << endl;

            }else{
                saldo += saldo_ingresado;
                registrartransacciones("Deposito: ", saldo_ingresado);
            }}
        double Saldo_cuenta(){
            return saldo;}
        
    }

;

int main(){

Cuenta cuenta(1000);
cuenta.Depositar(2000);
cuenta.Retirar(500);
cout << "Saldo actual: " << cuenta.Saldo_cuenta() << endl;
return 0;




}