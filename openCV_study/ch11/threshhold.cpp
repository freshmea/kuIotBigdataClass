
#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;
String folder = "/home/aa/kuIotBigdataClass/openCV_study/data/";

int main(int argc, char *argv[]) {
	// Mat src = imread(folder + "neutrophils.png", IMREAD_GRAYSCALE);
	Mat src;
	if (argc < 2) {
		src = imread(folder + "sudoku.jpg", IMREAD_GRAYSCALE);
	} else if (argc == 2) {
		src = imread(folder + argv[1], IMREAD_GRAYSCALE);
	} else {
		cerr << "usage: threshhold [image_path]" << endl;
		return -1;
	}
	if (src.empty()) {
		cerr << "Image load failed!" << endl;
		return -1;
	}

	int pos = 40;
	imshow("src", src);

	namedWindow("dst");
	createTrackbar("lower Hue", "dst", &pos, 179);

	while (true) {
		Mat dst;
		threshold(src, dst, pos, 255, THRESH_BINARY);
		imshow("dst", dst);
		if (waitKey(33) == 27) // break when ESC is pressed
			break;
	}
	destroyAllWindows();
	return 0;
}