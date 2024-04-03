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

    const int fps = 60;
    const std::chrono::milliseconds duration(1000 / fps);
    auto i = getTickCount();
    int keycode;
    while (true)
    {
        auto start = std::chrono::steady_clock::now();

        keycode = waitKey(1);

        cout << "keycode: " << keycode << endl;
        cout << "fps: " << getTickFrequency() / (getTickCount() - i) << endl;
        if (keycode == 'i' || keycode == 'I') {
            img = ~img;
            imshow("img", img);
        }
        else if (keycode == 27 || keycode == 'q' || keycode == 'Q') {
            break;
        }

        auto end = std::chrono::steady_clock::now();
        auto elapsed = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
        cout << "elapsed: " << elapsed.count() << endl;
        cout << "duration: " << duration.count() << endl;
        i = getTickCount();
        if (elapsed < duration) {
            std::this_thread::sleep_for(duration - elapsed);
        }
    }

    return 0;
}