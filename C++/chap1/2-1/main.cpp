#include <iostream>

/**
 * @brief "Hello, World!"와 입력 매개변수의 값을 출력합니다.
 * 
 * @param a 메시지와 함께 출력될 정수 값입니다.
 */
void print_hello_world(int a) {
    std::cout << "Hello, World!" << a <<std::endl;
}

int main() {
    int a = 0;
    for (int i = 0; i < 10; i++) {
        print_hello_world(a);
        a += 1;
    }
    return 0;
}