#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;
String folder = "/home/aa/kuIotBigdataClass/openCV_study/data/";
void on_brightness(int pos, void *userdata);

int main() {
	Mat src = imread(folder + "lenna.bmp", IMREAD_GRAYSCALE);
	int position = 256;
	namedWindow("img");
	createTrackbar("Brightness", "img", &position, 511, on_brightness,
				   (void *)&src);
	on_brightness(position, &src);
	waitKey();
	destroyAllWindows();
	return 0;
}

void on_brightness(int pos, void *userdata) {
	Mat img = *(Mat *)userdata;
	Mat dst = img + pos - 256;
	imshow("img", dst);
}