
#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;
String folder = "/home/aa/kuIotBigdataClass/openCV_study/data/";

int main() {
	Mat src = imread(folder + "keyboard.bmp", IMREAD_GRAYSCALE);
	Mat bin;
	threshold(src, bin, 0, 255, THRESH_BINARY | THRESH_OTSU);

	morphologyEx(bin, bin, MORPH_CLOSE, Mat(), Point(-1, -1), 3);

	Mat label2, stats, centroids;
	int cnt = connectedComponentsWithStats(bin, label2, stats, centroids, 8);

	Mat dst;
	cvtColor(bin, dst, COLOR_GRAY2BGR);
	cout << "number of labels: " << cnt << endl;
	for (int i = 1; i < cnt; i++) {
		int *p = stats.ptr<int>(i);
		if (p[4] < 20)
			continue;
		rectangle(dst, Rect(p[0], p[1], p[2], p[3]), Scalar(0, 0, 255));
		putText(dst, format("idx: %d centrois(%d, %d)", i, p[0], p[1]),
				Point(p[0], p[1]), FONT_HERSHEY_SIMPLEX, 0.4,
				Scalar(255, 0, 0));
	}
	imshow("bin", bin);
	imshow("src", src);
	imshow("dst", dst);
	waitKey();
	destroyAllWindows();
	return 0;
}