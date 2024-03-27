/**
 * @file main.cpp
 * @brief 프로그램의 진입점입니다.
 * @author 최수길
 * @date 2024-03-11
 * 이 함수는 프로그램의 진입점으로 사용됩니다. 콘솔에 "Hello, World!"와 "첫 번째 맛보기 C++ 프로그램입니다."를 출력합니다.
 */

#include <iostream>
#include <string>
#include <vector>

/**
 * @brief The main function of the program.
 * 
 * @return 0 
 */
int main() {
    char c[] = "hello";
    std::vector<char> v;
    v.push_back('h');
    v.push_back('e');
    v.push_back('l');
    std::cout << "Hello, World!" << std::endl;
    std::cout << "첫 번째 맛보기 C++ 프로그램입니다." << std::endl;
    std::string teststring(v.begin(), v.end());
    for (int i = 0; i < 10; i++){
        teststring += std::to_string(i);
        std::cout << teststring << std::endl;
    }
    for (auto i : v){
        teststring += i;
        std::cout << i << std::endl;
    }
    return 0;
}