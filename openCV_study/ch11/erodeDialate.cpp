
#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;
String folder = "/home/aa/kuIotBigdataClass/openCV_study/data/";

int main() {
	Mat src = imread(folder + "milkdrop.bmp");
	Mat bin;
	threshold(src, bin, 128, 255, THRESH_BINARY);

	Mat erodeMat, dilateMat;
	erode(bin, erodeMat, Mat());
	dilate(bin, dilateMat, Mat());

	imshow("bin", bin);
	imshow("erode", erodeMat);
	imshow("dilate", dilateMat);
	imshow("src", src);
	waitKey();
	destroyAllWindows();
	return 0;
}