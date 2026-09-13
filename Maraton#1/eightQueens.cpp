/*#include <iostream>
using namespace std;

int main() {
  cout << "Hello World!";
  return 0;
}*/

#include <iostream>
#include <list>
#include <algorithm> // Necesario para std::find

int main() {
    std::list<int> numeros = {10, 20, 30, 40};
    int buscando = 20;

    // Buscar el elemento
    auto it = std::find(numeros.begin(), numeros.end(), buscando);

    if (it != numeros.end()) {
        std::cout << "El elemento si esta en la lista.\n";
    } else {
        std::cout << "El elemento no esta en la lista.\n";
    }

    return 0;
}


