
#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;
String folder = "/home/aa/kuIotBigdataClass/openCV_study/data/";

int main() {
	Mat src = imread(folder + "rose.bmp", IMREAD_GRAYSCALE);

	vector<Mat> dsts;
	// filter2D(src, dst, -1, emboss, Point(-1, -1), 128);
	int sigma = 3;
	for (int alpha = 1; alpha <= 10; alpha += 1) {
		Mat blurred;
		GaussianBlur(src, blurred, Size(0, 0), sigma);
		alpha = float(alpha);
		Mat dst = (1 + alpha) * src - alpha * blurred;

		dsts.push_back(dst);
	}

	imshow("src", src);
	int i = 0;
	// type casting int to String
	for (auto dst : dsts) {
		imshow("dst" + to_string(i + 1), dst);
		i++;
	}

	waitKey();
	destroyAllWindows();
	return 0;
}