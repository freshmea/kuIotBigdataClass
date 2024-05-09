
#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;
String folder = "/home/aa/kuIotBigdataClass/openCV_study/data/";

int main() {
	Mat src = imread(folder + "coins.png", IMREAD_GRAYSCALE);

	blur(src, src, Size(3, 3));

	vector<Vec3f> circles;
	HoughCircles(src, circles, HOUGH_GRADIENT, 1, 50, 150, 30);

	Mat dst;
	cvtColor(src, dst, COLOR_GRAY2BGR);

	for (auto i : circles) {
		circle(dst, Point(cvRound(i[0]), cvRound(i[1])), cvRound(i[2]),
			   Scalar(0, 0, 255), 2);
	}

	imshow("src", src);
	imshow("dst", dst);
	waitKey();
	destroyAllWindows();
	return 0;
}