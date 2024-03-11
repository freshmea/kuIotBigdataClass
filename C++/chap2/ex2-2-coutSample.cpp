/**
 * @file area.cpp
 * @brief 원의 면적을 구하는 함수를 정의합니다.
 * @date 2024-03-11
 * @author 최수길
 * @
*/
#include <iostream>

/**
 * @brief 원의 면적을 구하는 함수입니다.
 * @param r 원의 반지름입니다.
 * @return 원의 면적을 반환합니다.
*/
double area(int r);

double area(int r) {
    return 3.14 * r * r;
}

/**
 * @brief 주어진 코드의 메인 함수입니다.
 * 
 * @return 0 프로그램이 성공적으로 종료되었음을 나타내는 값
 */
int main(){
    int n = 3;
    char c = '#';
    std::cout << c << 5.5 << '-' << n << "hello" << true << std::endl;
    std::cout << "n + 5 = " << n + 5 << '\n';
    std::cout << "면적은 " << area(n) << std::endl;
    return 0;
}