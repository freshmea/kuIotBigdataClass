#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace cv::dnn;
using namespace std;

void on_mouse(int event, int x, int y, int flags, void *userdata);

int main(int argc, char *argv[])
{
	if (argc < 2)
	{
		cerr << "Usage: " << argv[0] << " <model_path>" << endl;
		return -1;
	}

	// argv[1] is  .onnx file
	std::string filename = argv[1];
	// get extension before .
	std::string extension = filename.substr(filename.find_last_of(".") + 1);
	Net net;
	printf("extension: %s\n", extension.c_str());
	if (extension == "onnx")
	{
		net = readNetFromONNX(argv[1]);
		// argv[1] is .pb file
	}
	else if (extension == "pb")
	{
		net = readNet(argv[1]);
	}
	else
	{
		cerr << "Model file should be .onnx or .pb" << endl;
		return -1;
	}

	if (net.empty())
	{
		cerr << "Network load failed!" << endl;
		return -1;
	}

	Mat img = Mat::zeros(400, 400, CV_8UC1);

	imshow("img", img);
	setMouseCallback("img", on_mouse, (void *)&img);

	while (true)
	{
		int c = waitKey();

		if (c == 27)
		{
			break;
		}
		else if (c == ' ')
		{
			Mat blob = blobFromImage(img, 1 / 255.f, Size(28, 28));
			net.setInput(blob);
			Mat prob = net.forward();

			double maxVal;
			Point maxLoc;
			minMaxLoc(prob, NULL, &maxVal, NULL, &maxLoc);
			int digit = maxLoc.x;

			cout << digit << " (" << maxVal * 100 << "%)" << endl;

			img.setTo(0);
			imshow("img", img);
		}
	}

	return 0;
}

Point ptPrev(-1, -1);

void on_mouse(int event, int x, int y, int flags, void *userdata)
{
	Mat img = *(Mat *)userdata;
	static bool flag = false;
	if (event == EVENT_LBUTTONDOWN)
	{
		ptPrev = Point(x, y);
		flag = true;
	}
	else if (event == EVENT_LBUTTONUP)
	{
		ptPrev = Point(-1, -1);
		flag = false;
	}
	else if (event == EVENT_MOUSEMOVE && flag)
	{
		line(img, ptPrev, Point(x, y), Scalar::all(255), 40, LINE_AA, 0);
		ptPrev = Point(x, y);

		imshow("img", img);
	}
}
