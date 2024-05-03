#include "opencv2/opencv.hpp"
#include <iostream>
#include <string>

std::string folder = "/home/aa/kuIotBigdataClass/openCV_study/data/";

int main() {
  std::cout << "hello, World!" << std::endl;
  cv::Mat img;
  img = cv::imread(folder + "lenna.bmp");
  cv::imshow("image", img);
  cv::waitKey(0);
  return 0;
}