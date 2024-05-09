
#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;
String folder = "/home/aa/kuIotBigdataClass/openCV_study/data/";

int main() {
	Mat src = imread(folder + "circuit.bmp", IMREAD_COLOR);
	Mat temp1 = imread(folder + "crystal.bmp", IMREAD_COLOR);

	Mat res, resNorm;
	matchTemplate(src, temp1, res, TM_CCOEFF_NORMED);
	normalize(res, resNorm, 0, 255, NORM_MINMAX, CV_8U);

	double maxv;
	Point maxloc;
	minMaxLoc(res, NULL, &maxv, NULL, &maxloc);
	cout << "maxv: " << maxv << endl;

	rectangle(src, Rect(maxloc.x, maxloc.y, temp1.cols, temp1.rows),
			  Scalar(0, 0, 255), 2);
	imshow("resNorm", resNorm);
	imshow("src", src);
	waitKey();
	destroyAllWindows();
	return 0;
}