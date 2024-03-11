/**
 * @file Ex2-3-KeyInput.cpp
 * @brief cin << 을 활용한 프로그램
 * @author 최수길
 * @date 2024-03-11
*/

#include <iostream> 
using namespace std;
/**
 * @brief 주어진 코드의 메인 함수입니다.
 * @details 키보드로부터 너비와 높이를 입력받아 사각형의 면적을 계산합니다.
*/
int main() {
	cout << "너비를 입력하세요>>";

	int width;
	cin >> width; // 키보드로부터 너비를 읽어 width 변수에 저장

	cout << "높이를 입력하세요>>";

	int height;
	cin >> height; // 키보드로부터 높이를 읽어 height 변수에 저장

	int area = width*height; // 사각형의 면적 계산
	cout << "면적은 " << area << "\n"; // 면적을 출력하고 다음 줄로 넘어감
}