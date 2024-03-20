/**
 * @file main.cpp
 * @brief "Hello, World!"와 입력 매개변수의 값을 출력합니다.
 * @author 최수길
 * @date 2024-02-27
*/


#include "main.hpp"

/**
 * @brief A 클래스입니다.
 * @param a A 클래스의 멤버 변수입니다.
 * @param b A 클래스의 멤버 변수입니다.
 * @param A A 클래스의 생성자입니다.
 * @param print A 클래스의 멤버 함수입니다.
 
*/
class A {
    public:
    int a;
    int b;
    A() {
        a = 0;
        b = 0;
    }
    A(int a, int b) {
        this->a = a;
        this->b = b;
    }
    void print() {
        std::cout << a << " " << b << std::endl;
    }
};

/**
 * @brief "Hello, World!"와 입력 매개변수의 값을 출력합니다.
 * 
 * @param a 메시지와 함께 출력될 정수 값입니다.
 */
void print_hello_world(int a) {
    std::cout << "Hello, World!" << a <<std::endl;
}
/**
 * @brief main 함수입니다.
 * @return 정상 종료가 되면 0을 반환합니다.
*/
int main() {
    int a = 0;
    A b(1, 2);
    b.print();
    for (int i = 0; i < 10; i++) {
        print_hello_world(a);
        a += 1;
    }
    return 0;
}