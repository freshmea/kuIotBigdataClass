#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;
String folder = "/home/aa/kuIotBigdataClass/openCV_study/data/";

int main() {
	Mat src = imread(folder + "eastsea.bmp");

	vector<Mat> dsts;
	for (int i = 0; i < 3; i += 1) {
		Mat dst;
		flip(src, dst, i - 1);
		dsts.push_back(dst);
	}

	imshow("src", src);
	int i = 0;
	for (auto dst : dsts) {
		imshow("dst" + to_string(i + 1), dst);
		i++;
	}

	waitKey();
	destroyAllWindows();
	return 0;
}