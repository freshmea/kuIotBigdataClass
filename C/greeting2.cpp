#include <iostream>
#include <string>

using namespace std;
int main()
{
    cout <<"input your name : ";
    string name;
    cin >> name;

    string greeting = "Hello, " + name + "!";

    string line1 = string(greeting.size() + 4, '*');
    string line2= "* "+ string(greeting.size(), ' ')+ " *";
    string line3 = "* "+ greeting + " *";

    cout << line1 << endl;
    cout << line2 << endl;
    cout << line3 << endl;
    cout << line2 << endl;
    cout << line1 << endl;

    return 0;
}