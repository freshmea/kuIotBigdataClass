#include <iostream>
#include <vector>
#include <algorithm> // for_each() 알고리즘 함수를 사용하기 위함
using namespace std;

void print(int n) {
	cout << n << " ";
}

int main() {
	vector<int> v = { 1, 2, 3, 4, 5 };
	for_each(v.begin(), v.end(), print);
    for(auto i : v) {
        cout << i << " ";
    }
}
