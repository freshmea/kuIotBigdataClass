#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;
string folderPath = "/home/aa/kuIotBigdataClass/openCV/data/";

int main(void)
{
	Mat img = imread(folderPath+"lenna.bmp");

	if (img.empty()) {
		cerr << "Image load failed!" << endl;
		return -1;
	}

	namedWindow("img");
	imshow("img", img);
	auto i = getTickCount();
	int keycode;
	while (true)
	{
		keycode = waitKey(1);
		while(getTickFrequency() / (getTickCount() - i) > 60){
			// cout << "too high fps: " << getTickFrequency() / (getTickCount() - i) << endl;
		}
		cout << "keycode: " << keycode << endl;
		cout << "i: " << i << endl;
		cout << "fps: " << getTickFrequency() / (getTickCount() - i) << endl;
		// delay if fps is too high

		if (keycode == 'i' || keycode == 'I') {
			img = ~img;
			imshow("img", img);
		}
		else if (keycode == 27 || keycode == 'q' || keycode == 'Q') {
			break;
		}
		i=getTickCount();
	}

	return 0;
}
