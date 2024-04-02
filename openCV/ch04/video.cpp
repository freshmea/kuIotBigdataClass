#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

string folderPath = "/home/aa/kuIotBigdataClass/openCV/data/";

void camera_in();
void video_in();
void camera_in_video_out();

int main(void)
{
    camera_in();
    video_in();
    camera_in_video_out();
    return 0;
}


void camera_in()
{
    VideoCapture cap(4);

    if (!cap.isOpened()) {
        cerr << "Camera open failed!" << endl;
        return ;
    }

    cout << "Frame width: " << cvRound(cap.get(CAP_PROP_FRAME_WIDTH)) << endl;
    cout << "Frame height: " << cvRound(cap.get(CAP_PROP_FRAME_HEIGHT)) << endl;

    Mat frame, inversed;

    while (true) {
        cap >> frame;
        if (frame.empty())
            break;
        inversed = ~frame;

        imshow("frame", frame);
        imshow("inversed", inversed);

        if (waitKey(10) == 27)
            break;
    }

    destroyAllWindows();
}

void video_in()
{
    VideoCapture cap(folderPath+"vtest.avi");

    if (!cap.isOpened()) {
        cerr << "Video open failed!" << endl;
        return;
    }

    cout << "Frame width: " << cvRound(cap.get(CAP_PROP_FRAME_WIDTH)) << endl;
    cout << "Frame height: " << cvRound(cap.get(CAP_PROP_FRAME_HEIGHT)) << endl;
    cout << "Frame count: " << cvRound(cap.get(CAP_PROP_FRAME_COUNT)) << endl;

    Mat frame, inversed;

    while (true) {
        cap >> frame;
        if (frame.empty())
            break;
        inversed = ~frame;

        imshow("frame", frame);
        imshow("inversed", inversed);

        if (waitKey(10) == 27)
            break;
    }

    destroyAllWindows();
    // int XVID = cv::VideoWriter::fourcc('X', 'V', 'I', 'D'); // XVID MPEG-4
    // int MP4V = cv::VideoWriter::fourcc('M', 'P', '4', 'V'); // MPEG-4
    // int MJPG = cv::VideoWriter::fourcc('M', 'J', 'P', 'G'); // Motion-JPEG
    // int DIVX = cv::VideoWriter::fourcc('D', 'I', 'V', 'X'); // DIVX MPEG-4
    // int H264 = cv::VideoWriter::fourcc('H', '2', '6', '4'); // H.264
    // int X264 = cv::VideoWriter::fourcc('X', '2', '6', '4'); // H.264/AVC encoded with x264
    // int WMV1 = cv::VideoWriter::fourcc('W', 'M', 'V', '1'); // Windows Media Video 7
    // int WMV2 = cv::VideoWriter::fourcc('W', 'M', 'V', '2'); // Windows Media Video 8
}

void camera_in_video_out()
{
    VideoCapture cap(4);

    if (!cap.isOpened()) {
        cerr << "Camera open failed!" << endl;
        return ;
    }

    int w = cvRound(cap.get(CAP_PROP_FRAME_WIDTH));
    int h = cvRound(cap.get(CAP_PROP_FRAME_HEIGHT));
    double fps = cap.get(CAP_PROP_FPS);
    int fourcc = cv::VideoWriter::fourcc('D', 'I', 'V', 'X');
    int delay = cvRound(1000 / fps);

    VideoWriter outputVideo(folderPath+"output.avi", fourcc, fps, Size(w, h));

    if (!outputVideo.isOpened()) {
        cerr << "File open failed!" << endl;
        return ;
    }

    Mat frame, inversed;

    while (true) {
        cap >> frame;
        if (frame.empty())
            break;
        inversed = ~frame;

        outputVideo << inversed;

        imshow("frame", frame);
        imshow("inversed", inversed);

        if (waitKey(delay) == 27)
            break;
    }

    destroyAllWindows();
}