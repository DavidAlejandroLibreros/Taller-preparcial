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
    double Tasa_interes_anual;
    void registrartransaccionesnuevacuenta(string tipo, double saldo, double cantidad){
            ofstream archivo("Transacciones.txt", ios::app);
            if (archivo.is_open()){
                archivo << tipo << ": "<< cantidad << " .Nuevo saldo: " << saldo << endl;
                archivo.close();
            }else{
                cout << "No se pudo abrir el archivo de transacciones" << endl;

            }
            
            
            }
    public: // Vamos a suponer que la tasa de interes anual es del 5%
    CuentaDeposito(): Cuenta(), Impuesto(10), Tasa_interes_anual(0.05) {}
    CuentaDeposito(double saldo_inicial): Cuenta(saldo_inicial), Impuesto(10), Tasa_interes_anual(0.05){}
    
    void Retirar(double saldo_retirado){
        if(saldo_retirado + Impuesto > Saldo_cuenta()){
            cout << "Saldo insuficiente." << endl;
        } else {
            double Valor_total_retirado = saldo_retirado + Impuesto;
            double saldo = Saldo_cuenta() - Valor_total_retirado;
            registrartransaccionesnuevacuenta("Retiro con impuesto aplicado ", saldo , Valor_total_retirado);
        }
    }
    void AplicarInteresAnual(){
        double interes =  Saldo_cuenta() * Tasa_interes_anual;
        double saldo = Saldo_cuenta() - interes;
        registrartransaccionesnuevacuenta("Interes Anual acumulado cobrado", saldo, interes);




    }




};

int main(){

Cuenta Cuenta1(1000);
CuentaDeposito CuentaADepositar(2000);
CuentaADepositar.Depositar(1000);
CuentaADepositar.AplicarInteresAnual();
return 0;




}