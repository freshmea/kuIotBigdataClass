#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;
String folderPath = "/home/aa/kuIotBigdataClass/openCV/data/";
void hough_lines();
void hough_line_segments();
void hough_circles();
void hough_circles_trackbar();
void hough_circles_trackbar2();
void hough_circles_trackbar20();

int main(void)
{
	hough_lines();
	hough_line_segments();
	hough_circles();
	hough_circles_trackbar();
	hough_circles_trackbar2();
	// hough_circles_trackbar20();

	return 0;
}

void hough_lines()
{
	Mat src = imread(folderPath+"building.jpg", IMREAD_GRAYSCALE);

	if (src.empty()) {
		cerr << "Image load failed!" << endl;
		return;
	}

	Mat edge;
	Canny(src, edge, 50, 150);

	vector<Vec2f> lines;
	HoughLines(edge, lines, 1, CV_PI / 180, 250);

	Mat dst;
	cvtColor(edge, dst, COLOR_GRAY2BGR);

	for (size_t i = 0; i < lines.size(); i++) {
		float rho = lines[i][0], theta = lines[i][1];
		float cos_t = cos(theta), sin_t = sin(theta);
		float x0 = rho * cos_t, y0 = rho * sin_t;
		float alpha = 1000;

		Point pt1(cvRound(x0 - alpha * sin_t), cvRound(y0 + alpha * cos_t));
		Point pt2(cvRound(x0 + alpha * sin_t), cvRound(y0 - alpha * cos_t));
		line(dst, pt1, pt2, Scalar(0, 0, 255), 2, LINE_AA);
	}

	imshow("src", src);
	imshow("dst", dst);

	waitKey();
	destroyAllWindows();
}

void hough_line_segments()
{
	Mat src = imread(folderPath+"building.jpg", IMREAD_GRAYSCALE);

	if (src.empty()) {
		cerr << "Image load failed!" << endl;
		return;
	}

	Mat edge;
	Canny(src, edge, 50, 150);

	vector<Vec4i> lines;
	HoughLinesP(edge, lines, 1, CV_PI / 180, 160, 50, 5);

	Mat dst;
	cvtColor(edge, dst, COLOR_GRAY2BGR);

	for (Vec4i l : lines) {
		line(dst, Point(l[0], l[1]), Point(l[2], l[3]), Scalar(0, 0, 255), 2, LINE_AA);
	}

	imshow("src", src);
	imshow("dst", dst);

	waitKey();
	destroyAllWindows();
}

void hough_circles()
{
	Mat src = imread(folderPath+"coins.png", IMREAD_GRAYSCALE);

	if (src.empty()) {
		cerr << "Image load failed!" << endl;
		return;
	}

	Mat blurred;
	blur(src, blurred, Size(3, 3));

	vector<Vec3f> circles;
	HoughCircles(blurred, circles, HOUGH_GRADIENT, 1, 50, 150, 30);

	Mat dst;
	cvtColor(src, dst, COLOR_GRAY2BGR);

	for (Vec3f c : circles) {
		Point center(cvRound(c[0]), cvRound(c[1]));
		int radius = cvRound(c[2]);
		circle(dst, center, radius, Scalar(0, 0, 255), 2, LINE_AA);
	}

	imshow("src", src);
	imshow("dst", dst);

	waitKey();
	destroyAllWindows();
}

void hough_circles_trackbar()
{
	Mat src = imread(folderPath+"coins.png", IMREAD_GRAYSCALE);

	if (src.empty()) {
		cerr << "Image load failed!" << endl;
		return;
	}

	Mat blurred;
	blur(src, blurred, Size(3, 3));

	int min_dist = 50;
	int param1 = 150;
	int param2 = 30;
	int min_radius = 20;
	int max_radius = 50;

	namedWindow("dst");
	createTrackbar("min_dist", "dst", &min_dist, 100);
	createTrackbar("param1", "dst", &param1, 200);
	createTrackbar("param2", "dst", &param2, 100);
	createTrackbar("min_radius", "dst", &min_radius, 50);
	createTrackbar("max_radius", "dst", &max_radius, 100);

	while (true) {
		vector<Vec3f> circles;
		HoughCircles(blurred, circles, HOUGH_GRADIENT, 1, min_dist, param1, param2, min_radius, max_radius);

		Mat dst;
		cvtColor(src, dst, COLOR_GRAY2BGR);

		for (Vec3f c : circles) {
			Point center(cvRound(c[0]), cvRound(c[1]));
			int radius = cvRound(c[2]);
			circle(dst, center, radius, Scalar(0, 0, 255), 2, LINE_AA);
		}

		imshow("dst", dst);

		if (waitKey(1) == 27) break;
	}

	destroyAllWindows();
}


// 구조체로 정보 넘기기.
void hough_circles_trackbar_onChange(int, void*);
struct HoughCirclesTrackbarHandler{
	int min_dist = 50;
	int param1 = 150;
	int param2 = 30;
	int min_radius = 20;
	int max_radius = 50;
	Mat *blurred = 0;
	Mat *src = 0;
};

void hough_circles_trackbar2()
{
	Mat src = imread(folderPath + "coins.png", IMREAD_GRAYSCALE);
	Mat blurred;
	HoughCirclesTrackbarHandler handler;
	blur(src, blurred, Size(3, 3));
	handler.blurred = &blurred;
	handler.src = &src;

	if (src.empty()) {
		cerr << "Image load failed!" << endl;
		return;
	}


	namedWindow("dst");
	createTrackbar("min_dist", "dst", &handler.min_dist, 400, hough_circles_trackbar_onChange, &handler);
	createTrackbar("param1", "dst", &handler.param1, 400, hough_circles_trackbar_onChange, &handler);
	createTrackbar("param2", "dst", &handler.param2, 400, hough_circles_trackbar_onChange, &handler);
	createTrackbar("min_radius", "dst", &handler.min_radius, 400, hough_circles_trackbar_onChange, &handler);
    createTrackbar("max_radius", "dst", &handler.max_radius, 400, hough_circles_trackbar_onChange, &handler);

    hough_circles_trackbar_onChange(0, &handler); // initial call

    waitKey();
    destroyAllWindows();

    return;
}

void hough_circles_trackbar_onChange(int, void* handler)
{
	HoughCirclesTrackbarHandler *hcth = reinterpret_cast<HoughCirclesTrackbarHandler*>(handler);
    vector<Vec3f> circles;
	printf("min_dist: %d, param1: %d, param2: %d, min_radius: %d, max_radius: %d\n", hcth->min_dist, hcth->param1, hcth->param2, hcth->min_radius, hcth->max_radius);
	HoughCircles(*(hcth->blurred), circles, HOUGH_GRADIENT, 1, hcth->min_dist, hcth->param1, hcth->param2, hcth->min_radius, hcth->max_radius);

	Mat dst;
    cvtColor(*(hcth->src), dst, COLOR_GRAY2BGR);

    for (Vec3f c : circles) {
        Point center(cvRound(c[0]), cvRound(c[1]));
        int radius = cvRound(c[2]);
        circle(dst, center, radius, Scalar(0, 0, 255), 2, LINE_AA);
    }

    imshow("dst", dst);
}