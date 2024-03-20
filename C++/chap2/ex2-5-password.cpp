/**
 * @file ex2-5-password.cpp
 * @brief 암호를 입력받아 프로그램을 종료하는 프로그램
 * @author 최수길
 * @date 2024-03-11
 * 이 프로그램은 사용자로부터 암호를 입력받아, 암호가 맞으면 프로그램을 종료합니다.
 * 암호는 "C++"입니다.
 */

#include <iostream>
#include <cstring>
using namespace std;

/**
 * @brief 메인 함수
 * 
 * 사용자로부터 암호를 입력받아, 암호가 맞으면 프로그램을 종료하는 함수입니다.
 * 
 * @return int 프로그램 종료 시 반환되는 값
 */
int main() {
    char password[11];
    cout << "프로그램을 종료하려면 암호를 입력하세요." << endl;
    while(true) {
        cout << "암호>>";
        cin >> password;
        if(strcmp(password, "C++") == 0) {
            cout << "프로그램을 정상 종료합니다." << endl;
            break;
        }
        else 
            cout << "암호가 틀립니다~~" << endl;
    }
}