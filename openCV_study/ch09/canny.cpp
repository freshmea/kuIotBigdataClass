
#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;
String folder = "/home/aa/kuIotBigdataClass/openCV_study/data/";

int main() {
	Mat src = imread(folder + "lenna.bmp", IMREAD_GRAYSCALE);
	Mat dst1, dst2;

	Canny(src, dst1, 50, 100);
	Canny(src, dst2, 100, 150);
	imshow("dst1", dst1);
	imshow("dst2", dst2);
	imshow("src", src);
	waitKey();
	destroyAllWindows();
	return 0;
}