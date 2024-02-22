#include <iostream>
#include <string>

using namespace std;

int main()
{
    cout <<"input your name : ";
    string name;
    cin >> name;

    const string greeting = "Hello, " + name + "!";

    const int pad = 1;
    const int rows = 2 * pad +3;
    //const int cols = greeting.size() + 2 * pad + 2; 엄격하게 타입을 씀.
    const std::string::size_type cols = greeting.size() +2* pad +2;

    for(int r = 0 ; r != rows; ++r){
        std::string::size_type c = 0;
        while (c != cols){
            if(r == rows/2 && c == pad+1){
                cout << greeting;
                c = c + greeting.size();
            } else {
                if(r == 0 || r == rows-1 || c ==0 || c == cols-1){
                    cout << '*';
                }else {
                    cout << ' ';
                }
                ++c;
            }
        }
        cout << endl;
    }

    return 0;
}