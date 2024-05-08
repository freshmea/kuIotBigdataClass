#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;
String folder = "/home/aa/kuIotBigdataClass/openCV_study/data/";

int main() {
	Mat src = imread(folder + "lenna.bmp", IMREAD_GRAYSCALE);
	Mat original = src.clone();
	Mat src2 = src.clone();
	src = src * 2.f;				  // 1번째 방법
	src2 = src2 + (src2 - 180) * 1.f; // 2번째 방법

	cout << "original mean : " << mean(original) << endl;
	imshow("original", original);
	imshow("src", src);
	imshow("src2", src2);
	waitKey();
	destroyAllWindows();
	return 0;
}