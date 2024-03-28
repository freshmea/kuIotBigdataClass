#include "opencv2/opencv.hpp"
#include <iostream>
#include <string>

std::string folderPath = "/home/bindsoft/choisugil/kuIotBigdataClass/openCV/ch02/";
int main()
{
	std::cout << "Hello OpenCV " << CV_VERSION << std::endl;

	cv::Mat img;
	img = cv::imread(folderPath + "lenna.bmp");

	if (img.empty()) {
		std::cerr << "Image load failed!" << std::endl;
		return -1;
	}

	cv::namedWindow("image");
	cv::imshow("image", img);

	cv::waitKey();

	return 0;
}
