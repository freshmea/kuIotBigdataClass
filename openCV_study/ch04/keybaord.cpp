#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;
String folder = "/home/aa/kuIotBigdataClass/openCV_study/data/";

int main() {
	Scalar white = Scalar(255, 255, 255);
	Scalar yellow = Scalar(0, 255, 255);
	Scalar blue = Scalar(255, 0, 0);
	Scalar green = Scalar(0, 255, 0);
	Scalar red = Scalar(0, 0, 255);
	Mat img = imread(folder + "lenna.bmp");
	int keycode;

	namedWindow("img");
	imshow("img", img);
	while (true) {
		keycode = waitKey(33);
		cout << "keycode: " << keycode << endl;
		if (keycode == 27)
			break; // ESC
		else if (keycode == 'i' || keycode == 'I') {
			img = ~img;
			imshow("img", img);
		}
	}
	destroyAllWindows();
	return 0;
}