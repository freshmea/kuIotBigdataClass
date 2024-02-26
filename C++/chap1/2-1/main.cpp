#include <iostream>

int main() {
    int a = 0;
    for (int i = 0; i < 10; i++) {
        std::cout << "Hello, World!" << a <<std::endl;
        a += 1;
    }
    return 0;
}