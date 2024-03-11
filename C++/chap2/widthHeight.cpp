#include <iostream>
#include <cstring>
using namespace std;

int main(){
    cout << "너비를 입력하세요>>";
    int width;
    cin >> width;
    cout << "높이를 입력하세요>>";
    int height;
    cin >> height;
    int area = width * height;
    cout << "직사각형의 면적은 " << area << "입니다." << endl;
    return 0;
}