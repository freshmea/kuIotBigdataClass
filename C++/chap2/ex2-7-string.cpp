/**
 * @file ex2-7-string.cpp
 * @brief 사용자로부터 가수 이름을 입력받아 맞는지 확인하는 프로그램
 * @author 최수길
 * @date 2024-03-11
 * 이 프로그램은 사용자로부터 가수 이름을 입력받아, 그 이름이 맞는지 확인합니다.
 * 가수 이름은 "Elvis Presley"입니다.
 */

#include <iostream>
#include <string>
using namespace std;

/**
 * @brief 메인 함수
 * 사용자로부터 가수 이름을 입력받아 맞는지 확인하는 함수입니다.
 * @return int 프로그램 종료 시 반환되는 값
 */
int main() {
    string song("Falling in love with you"); // 문자열 song
    string elvis("Elvis Presley"); // 문자열 elvis
    string singer; // 문자열 singer

    cout << song + "를 부른 가수는"; // + 로 문자열 연결
    cout << "(힌트 : 첫글자는 " << elvis[0] << ")?";  // [] 연산자 사용

    getline(cin, singer); // 문자열 입력
    if(singer == elvis)  // 문자열 비교
            cout << "맞았습니다.";
    else
            cout << "틀렸습니다. "+ elvis + "입니다." << endl; // +로 문자열 연결
}