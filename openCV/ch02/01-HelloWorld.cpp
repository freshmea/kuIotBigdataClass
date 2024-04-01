#include "opencv2/opencv.hpp"
#include <iostream>
#include <string>
using namespace cv;
using namespace std;

string folderPath = "/home/aa/kuIotBigdataClass/openCV/data/";

std::string folderPath = "/home/bindsoft/choisugil/kuIotBigdataClass/openCV/ch02/";
int main()
{
	cout << "Hello OpenCV " << CV_VERSION << endl;
	Mat img;
	// IMREAD_ 로 시작하는 enum 상수를 사용하면 이미지를 읽을 때 다양한 옵션을 사용할 수 있다.
	img = imread(folderPath + "lenna.bmp", IMREAD_IGNORE_ORIENTATION | IMREAD_COLOR);
	Point pt1(10, 10);
	if (img.empty()) {
		cerr << "Image load failed!" << endl;
		return -1;
	}
	img.empty();

	imwrite(folderPath + "lenna.bmp", img, {IMWRITE_JPEG_QUALITY, 90, IMWRITE_PNG_COMPRESSION, 9});
	namedWindow("image", WINDOW_AUTOSIZE);
	Size size(640, 480);
	resizeWindow("image", size);
	imshow("image", img);

	waitKey();

	return 0;
}
