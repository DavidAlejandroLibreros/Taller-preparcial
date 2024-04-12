#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    const string caracteres_posibles = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+";
    srand(time(0)); // Inicializar la semilla para generar números aleatorios

    int longitud_minima = 8; // Longitud mínima de la contraseña
    int longitud_maxima = 12; // Longitud máxima de la contraseña
    int longitud = rand() % (longitud_maxima - longitud_minima + 1) + longitud_minima; // Generar una longitud aleatoria dentro del rango

    string contrasena;

    while (contrasena.length() < longitud) {
        int indice_aleatorio = rand() % caracteres_posibles.length(); // Generar un índice aleatorio dentro del rango de caracteres_posibles
        contrasena += caracteres_posibles[indice_aleatorio]; // Agregar un carácter aleatorio a la contraseña
    }

    cout << "La contraseña generada es: " << contrasena << endl;

    return 0;
}