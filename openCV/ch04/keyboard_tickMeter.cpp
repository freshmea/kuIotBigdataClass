#include "opencv2/opencv.hpp"
#include <iostream>
#include <chrono>
#include <thread>

using namespace cv;
using namespace std;
string folderPath = "/home/aa/kuIotBigdataClass/openCV/data/";

int main(void)
{
    Mat img = imread(folderPath+"lenna.bmp");

    if (img.empty()) {
        cerr << "Image load failed!" << endl;
        return -1;
    }

    namedWindow("img");
    imshow("img", img);

    const float fps = 60.0;
    TickMeter tm;
    TickMeter tm2;
    int keycode;
    while (true)
    {
        tm.start();
        tm2.start();

        keycode = waitKey(1);

        cout << "keycode: " << keycode << endl;
        cout << "fps: " << tm.getFPS() << endl;
        if (keycode == 'i' || keycode == 'I') {
            img = ~img;
            imshow("img", img);
        }
        else if (keycode == 27 || keycode == 'q' || keycode == 'Q') {
            break;
        }
        tm.stop();
        if (tm.getFPS() > fps) {
            auto sleep_duration = static_cast<int>(1000*(tm.getFPS() - fps)/tm.getFPS()/fps);
            std::this_thread::sleep_for(std::chrono::milliseconds(sleep_duration));
        }
        tm2.stop();
        cout << "fps2: " << tm2.getFPS() << endl;
    }

    return 0;
}