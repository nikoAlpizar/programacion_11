
#include <iostream>

using namespace std;

int main() {
    double num1, num2, suma, multiplicacion;
    cout << "Ingrese el primer numero: ";
    cin >> num1;
    cout << "Ingrese el segundo numero: ";
    cin >> num2;
    suma = num1 + num2;
    multiplicacion = num1 * num2;
    cout << "La suma de " << num1 << " y " << num2 << " es: " << suma << endl;
    cout << "La multiplicacion de " << num1 << " y " << num2 << " es: " << multiplicacion << endl;

    return 0;
}