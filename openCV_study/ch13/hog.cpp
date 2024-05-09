
#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;
String folder = "/home/aa/kuIotBigdataClass/openCV_study/data/";

int main() {
	VideoCapture cap(folder + "vtest.avi");

	HOGDescriptor hog;
	hog.setSVMDetector(HOGDescriptor::getDefaultPeopleDetector());
	Mat frame;
	while (true) {
		cap >> frame;
		if (frame.empty())
			break;
		vector<Rect> detected;
		hog.detectMultiScale(frame, detected);
		for (Rect r : detected) {
			rectangle(frame, r, Scalar(0, 0, 255), 2);
		}
		imshow("frame", frame);
		if (waitKey(30) == 27)
			break;
	}

	waitKey();
	destroyAllWindows();
	return 0;
}