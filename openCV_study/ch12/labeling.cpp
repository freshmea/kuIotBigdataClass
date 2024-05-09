
#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;
String folder = "/home/aa/kuIotBigdataClass/openCV_study/data/";

int main() {
	uchar data[] = {0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0,
					1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0,
					0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0,
					0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0};
	Mat src = Mat(8, 8, CV_8UC1, data);
	Mat label;
	int cnt = connectedComponents(src, label);
	cout << "number of labels: " << cnt << endl;
	cout << "label: \n" << label << endl;

	Mat label2, stats, centroids;
	int cnt2 = connectedComponentsWithStats(src, label2, stats, centroids, 8);
	cout << "number of labels: " << cnt2 << endl;
	cout << "label: \n" << label2 << endl;
	cout << "stats: \n" << stats << endl;
	cout << "centroids: \n" << centroids << endl;
	waitKey();
	destroyAllWindows();
	return 0;
}