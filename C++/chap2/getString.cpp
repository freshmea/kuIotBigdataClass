#include <iostream>
#include <string>

using namespace std;

int main(){
    string *name = new string[3];
    cout << "이름을 입력하세요 string>>";
    cin >> name[0];
    cout << "안녕하세요, " << name[0] << "씨" << endl;
    name[1] = "홍길동";
    cout << "안녕하세요, " << name[1] << "씨" << endl;
    delete[] name;
    cout << "안녕하세요, " << name[1] << "씨" << endl;
    name[1] += "hihihi";
    // cout << "안녕하세요, " << name[3] << "씨" << endl;
    // char name2[5];
    // cout << "이름을 입력하세요 char>>";
    // cin >> name2;
    // cout << "안녕하세요, " << name2 << "씨" << endl;
    string *test = new string[3];
    test[1] = "hello";
    test[1] += " world";
    cout << test[1] << endl;

    return 0;
}