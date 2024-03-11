/**
 * @file ex2-6-getline.cpp
 * @brief 사용자로부터 주소를 입력받아 출력하는 프로그램
 * @author 최수길
 * @date 2024-03-11
 * 이 프로그램은 사용자로부터 주소를 입력받아, 그 주소를 출력합니다.
 * 주소는 최대 100글자까지 입력받을 수 있습니다.
 */

#include <iostream>
using namespace std;

/**
 * @brief 메인 함수
 * 
 * 사용자로부터 주소를 입력받아 출력하는 함수입니다.
 * 
 * @return int 프로그램 종료 시 반환되는 값
 */
int main() {
    cout << "주소를 입력하세요>>";

    char address[100]; 
    cin.getline(address, 100, '\n'); // 키보드로부터 주소 읽기

    cout << "주소는 " << address << "입니다\n"; // 주소 출력
}