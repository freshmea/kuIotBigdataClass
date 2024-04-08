#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;
String folderPath = "/home/aa/kuIotBigdataClass/openCV/data/";

void color_op();
void color_inverse();
void color_grayscale();
void color_split();

int main(void)
{
	color_op();
	color_inverse();
	color_grayscale();
	color_split();

	return 0;
}

void color_op()
{
	Mat img = imread(folderPath+"butterfly.jpg", IMREAD_COLOR);

	if (img.empty()) {
		cerr << "Image load failed!" << endl;
		return;
	}

	Vec3b& pixel = img.at<Vec3b>(0, 0);
	uchar b1 = pixel[0];
	uchar g1 = pixel[1];
	uchar r1 = pixel[2];

	Vec3b* ptr = img.ptr<Vec3b>(0);
	uchar b2 = ptr[0][0];
	uchar g2 = ptr[0][1];
	uchar r2 = ptr[0][2];
}

void color_inverse()
{
	Mat src = imread(folderPath+"butterfly.jpg", IMREAD_COLOR);

	if (src.empty()) {
		cerr << "Image load failed!" << endl;
		return;
	}

	Mat dst(src.rows, src.cols, src.type());

	for (int j = 0; j < src.rows; j++) {
		for (int i = 0; i < src.cols; i++) {
			Vec3b& p1 = src.at<Vec3b>(j, i);
			Vec3b& p2 = dst.at<Vec3b>(j, i);

			p2[0] = 255 - p1[0]; // B
			p2[1] = 255 - p1[1]; // G
			p2[2] = 255 - p1[2]; // R
		}
	}

	imshow("src", src);
	imshow("dst", dst);

	waitKey();
	destroyAllWindows();
}

void color_grayscale()
{
	Mat src = imread(folderPath+"butterfly.jpg");

	if (src.empty()) {
		cerr << "Image load failed!" << endl;
		return;
	}

	Mat dst;
	cvtColor(src, dst, COLOR_BGR2GRAY);

	imshow("src", src);
	imshow("dst", dst);

	waitKey();
	destroyAllWindows();
}

void color_split()
{
	Mat src = imread(folderPath+"candies.png");

	if (src.empty()) {
		cerr << "Image load failed!" << endl;
		return;
	}

	vector<Mat> bgr_planes, b_planes, g_planes, r_planes;
	split(src, bgr_planes);
	Mat Bdst, Gdst, Rdst;
	Mat Empty(src.rows, src.cols, CV_8UC1, Scalar(0));
	b_planes = { bgr_planes[0], Empty, Empty };
	g_planes = { Empty, bgr_planes[1], Empty };
	r_planes = { Empty, Empty, bgr_planes[2] };
	merge(b_planes, Bdst);
	merge(g_planes, Gdst);
	merge(r_planes, Rdst);
	imshow("src", src);
	imshow("B_plane", Bdst);
	imshow("G_plane", Gdst);
	imshow("R_plane", Rdst);

	waitKey();
	destroyAllWindows();
}