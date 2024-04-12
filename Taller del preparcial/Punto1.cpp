#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int a, b, c;

    cout << "Introduce el valor de a: ";
    cin >> a;

    cout << "Introduce el valor de b: ";
    cin >> b;

    cout << "Introduce el valor de c: ";
    cin >> c;

    int discriminante = b*b - 4*a*c;

    if (discriminante < 0) {
        cout << "La ecuación no tiene solución" << endl;
    } else if (discriminante > 0) {
        float w = sqrt(discriminante);

        cout << "La ecuación tiene dos soluciones:" << endl;

        float Sol1 = (-b + w) / (2*a);
        float Sol2 = (-b - w) / (2*a);

        cout << "Si tomamos a " << w << " como positivo, entonces la solución de la ecuación es " << Sol1 << endl;
        cout << "Si tomamos a " << w << " como negativo, entonces la solución de la ecuación es " << Sol2 << endl;
    } else {
        
        float Sol3 = -b / (2*a);

        cout << "La solución de la ecuación es " << Sol3 << endl;

        return 0;
    }
}