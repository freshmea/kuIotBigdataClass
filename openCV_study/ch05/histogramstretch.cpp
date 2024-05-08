#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;
String folder = "/home/aa/kuIotBigdataClass/openCV_study/data/";
void histogramGraph(Mat &graph, const Mat &src);

int main() {
	Mat src = imread(folder + "hawkes.bmp", IMREAD_GRAYSCALE);
	double gmin, gmax;
	minMaxLoc(src, &gmin, &gmax);
	Mat dst = (src - gmin) * 255 / (gmax - gmin);

	Mat graphSrc(100, 256, CV_8U, Scalar(255));
	Mat graphDst(100, 256, CV_8U, Scalar(255));

	histogramGraph(graphSrc, src);
	histogramGraph(graphDst, dst);

	resize(src, src, Size(800, 800));
	resize(dst, dst, Size(800, 800));
	imshow("src", src);
	imshow("dst", dst);
	imshow("graphSrc", graphSrc);
	imshow("graphDst", graphDst);
	waitKey();
	destroyAllWindows();
	return 0;
}

void histogramGraph(Mat &graph, const Mat &src) {
	Mat histo;
	int channels[] = {0};
	int dims = 1;
	const int histSize[] = {256};
	float graylevel[] = {0, 256};
	const float *ranges[] = {graylevel};

	calcHist(&src, 1, channels, noArray(), histo, dims, histSize, ranges);

	// make graph histogram
	normalize(histo, histo, 0, 100, NORM_MINMAX);
	for (int i = 0; i < 256; i++) {
		line(graph, Point(i, 100), Point(i, 100 - cvRound(histo.at<float>(i))),
			 Scalar(0));
	}
}