#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;
String folderPath = "/home/aa/kuIotBigdataClass/openCV/data/";

void filter_embossing();
void myFilter2D(const cv::Mat& src, cv::Mat& dst, const cv::Mat& kernel);
void myCopyMakeBorder(const cv::Mat& src, cv::Mat& dst, int top, int bottom, int left, int right);

int main(void)
{
	filter_embossing();

	return 0;
}

void filter_embossing()
{
	Mat src = imread(folderPath+"rose.bmp", IMREAD_GRAYSCALE);

	if (src.empty()) {
		cerr << "Image load failed!" << endl;
		return;
	}

	float data[] = { -1, -1, 0, -1, 0, 1, 0, 1, 1 };
	Mat emboss(3, 3, CV_32FC1, data);

	// Mat dst;
	Mat dst = cv::Mat::zeros(src.size(), src.type());
	filter2D(src, dst, -1, emboss, Point(-1, -1), 0, BORDER_REPLICATE);
	myFilter2D(src, dst, emboss);
	// dst += 128;
	imshow("src", src);
	imshow("dst", dst);

	waitKey();
	destroyAllWindows();
}

void myFilter2D(const cv::Mat& src, cv::Mat& dst, const cv::Mat& kernel) {
    int kHalfX = kernel.cols / 2;
    int kHalfY = kernel.rows / 2;
	float kernelSize = kernel.rows * kernel.cols;

	cv::Mat srcPadded;
	myCopyMakeBorder(src, srcPadded, kHalfY, kHalfY, kHalfX, kHalfX);
    dst = cv::Mat::zeros(src.size(), src.type());

    for (int y = 0; y < src.rows; y++) {
        for (int x = 0; x < src.cols; x++) {
            float sum = 0.0f;

            for (int ky = -kHalfY; ky <= kHalfY; ky++) {
                for (int kx = -kHalfX; kx <= kHalfX; kx++) {
                    int iy = y + ky + kHalfY;
                    int ix = x + kx + kHalfX;
                    uint8_t pixel = srcPadded.at<uint8_t>(iy, ix);
                    float coeff = kernel.at<float>(ky + kHalfY, kx + kHalfX);
					sum += pixel * coeff/kernelSize;
				}
			}
			printf("sum: %f\n", sum);

            dst.at<uint8_t>(y, x) = sum;
        }
    }
}

void myCopyMakeBorder(const cv::Mat& src, cv::Mat& dst, int top, int bottom, int left, int right) {
    // Create a new matrix with the appropriate size and type
    dst.create(src.rows + top + bottom, src.cols + left + right, src.type());

    // Copy the source image into the center of the destination image
    src.copyTo(dst(cv::Rect(left, top, src.cols, src.rows)));

    // Create the border by replicating the edge pixels
    cv::Mat topRow = dst.row(top).clone();
    cv::Mat bottomRow = dst.row(dst.rows - bottom - 1).clone();
    cv::Mat leftCol = dst.col(left).clone();
    cv::Mat rightCol = dst.col(dst.cols - right - 1).clone();

    for (int i = 0; i < top; i++) {
        topRow.copyTo(dst.row(i));
    }
    for (int i = 0; i < bottom; i++) {
        bottomRow.copyTo(dst.row(dst.rows - i - 1));
    }
    for (int i = 0; i < left; i++) {
        leftCol.copyTo(dst.col(i));
    }
    for (int i = 0; i < right; i++) {
        rightCol.copyTo(dst.col(dst.cols - i - 1));
    }
}