#include <iostream>
#include <string>

int main()
{
    int edad;
    char tipo;
    int precio =100;
    
    
    std::cout<<"Ingresa tu edad";
    std::cin >> edad;
    
    std::cout<<"Ingresa el tipo \n N: Normal \n E: Estudiante \n S: Senior";
    std::cin >> tipo;
    
    
    if(tipo=='e'|| tipo=='E') {
        std::cout<<"Precio de entrada 50";
    }
    else if(edad<5){
        if(tipo!='s'|| tipo!='S'|| tipo!='e'|| tipo!='E'){
            std::cout<<"Precio de entrada 0";
        }
    }
    else if( edad>5 && edad<60) {
        if(tipo=='n'|| tipo=='N'){
        std::cout<<"Precio de entrada 100";    
        }
    }
    
    else if(edad>=60) {
        if(tipo=='s'|| tipo=='S'){
            std::cout<<"Precio de entrada 70";
        }
        else {
            std::cout<<"Precio de entrada 100";
        }
    }
    else if(tipo!='s'|| tipo!='S'|| tipo!='N'|| tipo!='n'|| tipo!='e'|| tipo!='E') {
        std::cout<<"Tipo de entrada no valida";
    }

    return 0;
}
