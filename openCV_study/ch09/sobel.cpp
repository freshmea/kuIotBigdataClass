
#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;
String folder = "/home/aa/kuIotBigdataClass/openCV_study/data/";

int main() {
	Mat src = imread(folder + "lenna.bmp", IMREAD_GRAYSCALE);

	Mat dx, dy;
	Sobel(src, dx, CV_32F, 1, 0);
	Sobel(src, dy, CV_32F, 0, 1);

	Mat dx8u, dy8u;
	dx.convertTo(dx8u, CV_8U);
	dy.convertTo(dy8u, CV_8U);

	Mat fmag, mag;
	magnitude(dx, dy, fmag);
	fmag.convertTo(mag, CV_8U);

	imshow("mag", mag);
	imshow("dx", dx8u);
	imshow("dy", dy8u);
	imshow("src", src);
	waitKey();
	destroyAllWindows();
	return 0;
}