#include "opencv2/opencv.hpp"
#include <iostream>
#include <chrono>
#include <thread>

using namespace cv;
using namespace std;
string folderPath = "/home/aa/kuIotBigdataClass/openCV/data/";

void set_fps_rapper_while(int fps, std::function<void()> func)
{
    const std::chrono::milliseconds duration(1000 / fps);
    auto start = std::chrono::steady_clock::now();
    func();
    auto end = std::chrono::steady_clock::now();
    auto elapsed = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
    if (elapsed < duration) {
        std::this_thread::sleep_for(duration - elapsed);
    }
}

void on_mouse(int event, int x, int y, int flags, void*)
{
    switch (event) {
    case EVENT_LBUTTONDOWN:
        cout << "EVENT_LBUTTONDOWN: " << x << ", " << y << endl;
        break;
    case EVENT_LBUTTONUP:
        cout << "EVENT_LBUTTONUP: " << x << ", " << y << endl;
        break;
    case EVENT_MOUSEMOVE:
        if (flags & EVENT_FLAG_LBUTTON) {
            cout << "EVENT_MOUSEMOVE: " << x << ", " << y << endl;
        }
        break;
    default:
        break;
    }
}

int main(void)
{
    Mat img = imread(folderPath+"lenna.bmp");

    if (img.empty()) {
        cerr << "Image load failed!" << endl;
        return -1;
    }

    namedWindow("img");
    imshow("img", img);

    auto i = getTickCount();
    bool play = true;
    int keycode;
    setMouseCallback("img", on_mouse);
    while (play)
    {
        set_fps_rapper_while(60, [&img, &i, &play, &keycode]()
                             {
            keycode = waitKey(3);
            // cout << "keycode: " << keycode << endl;
            // cout << "fps: " << getTickFrequency() / (getTickCount() - i) << endl;
            if (keycode == 'i' || keycode == 'I') {
                img = ~img;
                imshow("img", img);
            }
            else if (keycode == 27 ||  keycode == 'q' || keycode == 'Q') {
                play = false;
                return;
            }
            i = getTickCount();
             });
    }

    return 0;
}