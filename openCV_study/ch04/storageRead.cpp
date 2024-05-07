#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;
String folder = "/home/aa/kuIotBigdataClass/openCV_study/data/";
int main() {
	String name;
	int age;
	Point pt1;
	vector<int> v;
	Mat mat1;

	FileStorage fs;
	fs.open(folder + "mydata.json", FileStorage::READ);
	if (!fs.isOpened()) {
		cerr << "File open failed!" << endl;
		return 1;
	}

	fs["name"] >> name;
	fs["age"] >> age;
	fs["point"] >> pt1;
	fs["v"] >> v;
	fs["mat1"] >> mat1;

	fs.release();

	cout << "name: " << name << endl;
	cout << "age: " << age << endl;
	cout << "point: " << pt1 << endl;
	cout << "v: {";
	for (auto i : v) {
		cout << i << ", ";
	}
	cout << " }" << endl;
	cout << "mat1: " << mat1 << endl;
	return 0;
}