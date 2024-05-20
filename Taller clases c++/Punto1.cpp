#include <iostream>
#include <fstream>
using namespace std;

    class Cuenta{
        private:
        double saldo;
        void registrartransacciones(string tipo, double saldo, double cantidad){
            ofstream archivo("Transacciones.txt", ios::app);
            if (archivo.is_open()){
                archivo << tipo << ": "<< cantidad << " .Nuevo saldo: " << saldo << endl;
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

            } else{
            saldo = saldo - saldo_retirado;
            registrartransacciones("Retiro: ", saldo ,saldo_retirado);
            }}
        void Depositar(double saldo_ingresado){
            if(saldo_ingresado < 0){
                cout << "No puede ingresar un saldo negativo" << endl;

            }else{
                saldo += saldo_ingresado;
                registrartransacciones("Deposito: ", saldo ,saldo_ingresado);
            }}
        double Saldo_cuenta(){
            return saldo;}
        
    }

;
class CuentaDeposito: public Cuenta{
    private:
    double Impuesto;
    void registrartransaccionesnuevacuenta(string tipo, double saldo, double cantidad){
            ofstream archivo("Transacciones.txt", ios::app);
            if (archivo.is_open()){
                archivo << tipo << ": "<< cantidad << " .Nuevo saldo: " << saldo << endl;
                archivo.close();
            }else{
                cout << "No se pudo abrir el archivo de transacciones" << endl;

            }
            
            
            }
    public:
    CuentaDeposito(): Cuenta(), Impuesto(10) {}
    CuentaDeposito(double saldo_inicial): Cuenta(saldo_inicial), Impuesto(10){}
    
    void Retirar(double saldo_retirado){
        if(saldo_retirado + Impuesto > Saldo_cuenta()){
            cout << "Saldo insuficiente." << endl;
        } else {
            double saldo = Saldo_cuenta() - saldo_retirado - Impuesto;
            cout << saldo << endl;

        }


    }




};

int main(){


CuentaDeposito CuentaADepositar(2000);
CuentaADepositar.Retirar(600);
return 0;




}