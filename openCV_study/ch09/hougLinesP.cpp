
#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;
String folder = "/home/aa/kuIotBigdataClass/openCV_study/data/";

int main() {
	Mat src = imread(folder + "building.jpg", IMREAD_GRAYSCALE);
	Mat dst1, dst2;

	Mat edge;
	Canny(src, edge, 50, 150);

	vector<Vec4i> lines;
	HoughLinesP(edge, lines, 1, CV_PI / 180, 160, 50, 5);

	Mat dst;
	cvtColor(src, dst, COLOR_GRAY2BGR);

	for (auto i : lines) {
		line(dst, Point(i[0], i[1]), Point(i[2], i[3]), Scalar(0, 0, 255), 2);
	}

	imshow("edge", edge);
	imshow("src", src);
	imshow("dst", dst);
	waitKey();
	destroyAllWindows();
	return 0;
}