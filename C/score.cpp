#include <iostream>
#include <string>
using namespace std;

int main()
{
    string name;
    cin >> name;

    double midterm, finalterm;
    cin >> midterm >> finalterm;

    double sum = 0;
    double homework;
    int count = 0;
    while(cin >> homework){         //입력이 안되면 false 가 됨.
        sum += homework;
        ++count;
    }

    double average = sum / count;

    double final_score = .2 * midterm + .4 * finalterm + .4 * average;
    cout << "final score : " << final_score << endl;
    return 0;
}