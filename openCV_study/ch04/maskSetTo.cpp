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

	Mat img = imread(folder + "lenna.bmp", IMREAD_COLOR);
	Mat mask = imread(folder + "mask_smile.bmp", IMREAD_GRAYSCALE);
	Mat airplainImg = imread(folder + "airplane.bmp", IMREAD_COLOR);
	Mat fieldImg = imread(folder + "field.bmp", IMREAD_COLOR);
	Mat mask2 = imread(folder + "mask_plane.bmp", IMREAD_GRAYSCALE);

	img.setTo(yellow, mask);
	airplainImg.copyTo(fieldImg, mask2);

	imshow("img", img);
	imshow("fieldImg", fieldImg);
	waitKey(0);
	destroyAllWindows();
	return 0;
}