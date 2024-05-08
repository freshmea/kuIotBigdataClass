
#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;
String folder = "/home/aa/kuIotBigdataClass/openCV_study/data/";

int main() {
	Mat src = imread(folder + "tekapo.bmp");
	Point2d cp(src.cols / 2., src.rows / 2.);
	Mat M = getRotationMatrix2D(cp, 20, 0.7);

	Mat dst;
	warpAffine(src, dst, M, Size());

	imshow("src", src);
	imshow("dst", dst);
	waitKey();
	destroyAllWindows();
	return 0;
}