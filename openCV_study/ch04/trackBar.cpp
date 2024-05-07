#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;
String folder = "/home/aa/kuIotBigdataClass/openCV_study/data/";
void on_level_change(int pos, void *userdata);

int main() {
	Scalar white = Scalar(255, 255, 255);
	Scalar yellow = Scalar(0, 255, 255);
	Scalar blue = Scalar(255, 0, 0);
	Scalar green = Scalar(0, 255, 0);
	Scalar red = Scalar(0, 0, 255);
	Mat img(400, 400, CV_8UC3, white);

	namedWindow("img");
	createTrackbar("level", "img", 0, 255, on_level_change, &img);
	imshow("img", img);
	waitKey(0);
	destroyAllWindows();
	return 0;
}

void on_level_change(int pos, void *userdata) {
	Mat img = *(Mat *)userdata;
	Scalar gray = Scalar(pos, pos, pos);
	img.setTo(gray);
	imshow("img", img);
}