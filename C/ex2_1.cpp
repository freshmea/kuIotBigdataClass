#include <iostream>
#include <string>

using namespace std;

int main()
{
    cout <<"input your name : ";
    string name;
    cin >> name;

    const string greeting = "Hello, " + name + "!";

    const int pad = 2;
    const int rows = 2 * pad +3;
    const std::string::size_type cols = greeting.size() +2* pad +2;

    for(int r = 0 ; r != rows; ++r){
        string line;
        if(r == 0 || r == rows-1){
            line.assign(cols, '*');
        } else if(r == rows/2){
            line = "*"+string(pad, ' ')+greeting+string(pad, ' ')+"*";
        } else {
            line = "*"+string(cols-2, ' ')+"*";
        }
        cout << line <<endl;
    }

    return 0;
}